from my_home_handle import Handler
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='/tmp/twitter-connection.log',
                    filemode='w')

handler = Handler()

while True:
    try:
        handler.get_tweets()
        handler.save_tweets()
    except:
        handler.offset_file.close()