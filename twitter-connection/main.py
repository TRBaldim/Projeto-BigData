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