import twitter
import time
import logging
import sqlite3
from configparser import ConfigParser
from kafka import KafkaClient, SimpleProducer


class Handler:
    def __init__(self):
        cp = ConfigParser()
        cp.read('keys.cfg')

        self.conn = sqlite3.connect('offset.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS offsets
                                      (position TEXT, offset INTEGER)''')
        self.conn.commit()

        results = self.get_offsets()

        if results:
            self.actual_offset_start = results[0][1]
            self.actual_offset_ends = results[1][1]
            self.last_offset = results[2][1]
        else:
            self.cursor.execute('''INSERT INTO offsets VALUES ('start', 0)''')
            self.cursor.execute('''INSERT INTO offsets VALUES ('end', 0)''')
            self.cursor.execute('''INSERT INTO offsets VALUES ('last', 0)''')
            self.conn.commit()
            self.actual_offset_start = None
            self.actual_offset_ends = None
            self.last_offset = None
        # Kafka Connection
        kafka = KafkaClient('172.17.0.3:9092')
        self.producer = SimpleProducer(kafka)

        self.connector = twitter.Api(consumer_key=cp.get('keys', 'consumer_key'),
                                     consumer_secret=cp.get('keys', 'consumer_secret'),
                                     access_token_key=cp.get('keys', 'access_token_key'),
                                     access_token_secret=cp.get('keys', 'access_token_secret'))
        self.statuses_twitter = None
        self.running = False
        self.old_tweets_flag = False

    def get_offsets(self):
        self.cursor.execute('''SELECT * FROM offsets''')
        results = self.cursor.fetchall()
        if results:
            return results
        else:
            return None

    def update_offset(self, key, value):
        query = 'UPDATE offsets SET position = \"' + key + \
                '\", offset = ' + str(value) + \
                ' WHERE position = \"' + key + '\"'
        self.cursor.execute(query)
        self.conn.commit()

    def commit_offset(self, offset):
        '''
        Gerencia o offset de tweets caso haja alguma queda no processamento do dado.
        :param offset: id do ultimo tweet lido pela aplicacao
        :return: None
        '''
        self.actual_offset_ends = offset[len(offset) - 1]
        self.last_offset = offset[len(offset) - 1] if self.last_offset != 0 else 0
        if not self.old_tweets_flag:
            self.actual_offset_start = offset[0]
        else:
            self.actual_offset_start = self.actual_offset_start
            self.actual_offset_ends -= 1
        self.update_offset('start', self.actual_offset_start)
        self.update_offset('end', self.actual_offset_ends)
        self.update_offset('last', self.last_offset)

    def get_tweets(self):
        '''
        Recupera todos os tweets da minha timeline
        :return: None
        '''
        tweets = None
        if self.running:
            time.sleep(60)
        try:
            if self.old_tweets_flag and \
               self.actual_offset_ends <= self.last_offset:
                tweets = self.connector.GetHomeTimeline(count=200,
                                                        max_id=self.actual_offset_ends,
                                                        exclude_replies=True)
            elif not self.old_tweets_flag:
                tweets = self.connector.GetHomeTimeline(count=200,
                                                        since_id=self.actual_offset_start,
                                                        exclude_replies=True)
            else:
                tweets = []
        except twitter.TwitterError as e:
            logging.error('Excesso de chamadas para recuperar os tweets')
            logging.debug(e.message)
            time.sleep(900)

        finally:
            self.running = True
            self.statuses_twitter = tweets

    def get_old_tweets(self):
        pass

    def save_tweets(self):
        io_string = ''
        tweets_ids = set()
        count_tweets = 0
        commit_offset = False
        for t in self.statuses_twitter:
            tweet = t.AsDict()
            io_string += str(t)
            io_string += '\n'
            tweets_ids.add(tweet['id'])
            count_tweets += 1
        try:
            logging.info('Salvando Tweets total: ' + str(count_tweets))
            if count_tweets:
                self.producer.send_messages(b'twitter', str(io_string).encode('utf-8'))
            commit_offset = True
        except Exception as e:
            logging.error('Erro ao escrever no arquivo com Tweets', e.message)
            commit_offset = False
        if commit_offset:
            try:
                self.commit_offset(list(sorted(tweets_ids, reverse=True)))
                self.old_tweets_flag = False
                return commit_offset
            except Exception as e:
                if not self.old_tweets_flag:
                    self.old_tweets_flag = True
                else:
                    self.old_tweets_flag = False
                    self.last_offset = 0
                logging.info('Sem novos tweets')
                logging.debug(e.message)
                commit_offset = False
                return commit_offset
        else:
            return commit_offset



