import twitter
import time
from configparser import ConfigParser


class Handler:
    def __init__(self):
        cp = ConfigParser()
        cp.read('keys.cfg')

        try:
            self.offset_file = open('home.offset', 'r+')
        except IOError as e:
            print 'Nao foi possivel criar arquivo de offset'
            print e.message
            print 'Criando Arquivo'
            open('home.offset', 'a').close()
            self.offset_file = open('home.offset', 'r+')

        self.actual_offset = self.offset_file.readline()

        # TODO: Esta variavel sera alterada pela conexao com o kafka
        self.tweets_file = open('myfile.tweets', 'a')

        self.connector = twitter.Api(consumer_key=cp.get('keys', 'consumer_key'),
                                     consumer_secret=cp.get('keys', 'consumer_secret'),
                                     access_token_key=cp.get('keys', 'access_token_key'),
                                     access_token_secret=cp.get('keys', 'access_token_secret'))
        self.statuses_twitter = None
        self.running = False

    def commit_offset(self, offset):
        '''
        Gerencia o offset de tweets caso haja alguma queda no processamento do dado.
        :param offset: id do ultimo tweet lido pela aplicacao
        :return: None
        '''
        self.offset_file.seek(0)
        self.offset_file.write(str(offset))
        self.offset_file.truncate()
        self.offset_file.flush()
        self.actual_offset = offset

    def get_tweets(self):
        '''
        Recupera todos os tweets da minha timeline
        :return: None
        '''
        tweets = None
        if self.running:
            time.sleep(60)
        try:
            tweets = self.connector.GetHomeTimeline(count=200,
                                                    since_id=self.actual_offset,
                                                    exclude_replies=True)
        except twitter.TwitterError as e:
            print 'Excesso de chamadas para recuperar os tweets'
            print e.message
            time.sleep(901)
            tweets = self.connector.GetHomeTimeline(count=200,
                                                    since_id=self.actual_offset,
                                                    exclude_replies=True)
        finally:
            self.running = True
            self.statuses_twitter = tweets


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
            print 'Salvando Tweets'
            self.tweets_file.write(io_string)
            self.tweets_file.flush()
            commit_offset = True
        except Exception as e:
            raise Exception('Erro ao escrever no arquivo com Tweets', e.message)
        if commit_offset:
            try:
                self.commit_offset(list(sorted(tweets_ids, reverse=True))[0])
                return commit_offset
            except Exception as e:
                print 'Sem novos tweets, iniciando processo de tweets antigos'
                #TODO: Criar metodo para gerenciar tweets antigos
                print e.message
                commit_offset = False
                return commit_offset



