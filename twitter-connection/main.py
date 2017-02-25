import twitter
from configparser import ConfigParser
import time
from my_home_handle import Handler


handler = Handler()

while True:
    try:
        handler.get_tweets()
        handler.save_tweets()
    except:
        handler.offset_file.close()
        handler.tweets_file.close()

'''
f = open('myfile.tweets', 'w')

cp = ConfigParser()

cp.read('keys.cfg')

api = twitter.Api(consumer_key=cp.get('keys', 'consumer_key'),
                  consumer_secret=cp.get('keys', 'consumer_secret'),
                  access_token_key=cp.get('keys', 'access_token_key'),
                  access_token_secret=cp.get('keys', 'access_token_secret'))

twitter_ids = [None]
while True:
    try:
        last_tweet_id = sorted(twitter_ids, reverse=True)[0]
    except:
        time.sleep(60)
        continue
    tweets = api.GetHomeTimeline(count=200,
                                 since_id=last_tweet_id,
                                 exclude_replies=True)
    twitter_ids = []
    for t in tweets:
        tweet_dict = t.AsDict()
        twitter_ids.append(tweet_dict['id'])
        f.write(str(tweet_dict))
        f.write('\n')
        try:
            number_of_retweets = tweet_dict['retweet_count']
            urls = tweet_dict['urls']
            if number_of_retweets >= 1:
                retweeted_id = tweet_dict['id']
                #print api.GetRetweeters(retweeted_id)
                print retweeted_id
                print urls
                #print api.GetRateLimitStatus()
        except:
            pass
    f.flush()
    time.sleep(60)

f.close()
'''