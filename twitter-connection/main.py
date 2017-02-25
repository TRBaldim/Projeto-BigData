import twitter
from configparser import ConfigParser
from twitter import Status

f = open('myfile.tweets', 'w')

cp = ConfigParser()

cp.read('keys.cfg')

api = twitter.Api(consumer_key=cp.get('keys', 'consumer_key'),
                  consumer_secret=cp.get('keys', 'consumer_secret'),
                  access_token_key=cp.get('keys', 'access_token_key'),
                  access_token_secret=cp.get('keys', 'access_token_secret'))

tweets = api.GetHomeTimeline(count=200, exclude_replies=True)

for t in tweets:
    tweet_dict = t.AsDict()
    f.write(str(tweet_dict))
    f.write('\n')
    try:
        number_of_retweets = tweet_dict['retweet_count']
        urls = tweet_dict['urls']
        if number_of_retweets > 3:
            retweeted_id = tweet_dict['id']
            #print api.GetRetweeters(retweeted_id)
            print retweeted_id
            print urls
    except:
        pass
f.close()
