from algorithms import knn
import re
import json
from unidecode import unidecode
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

def remove_http(s):
    text_list = re.sub("[^a-zA-Z]", " ", s[:s.find('http')]).lower().split()
    stops = set(stopwords.words('portuguese'))
    mean_words = [w for w in text_list if not w in stops]
    return " ".join(mean_words)


tweets = open('/home/thiago/Mestrado/topicos-BigData/Projeto-BigData/twitter-connection/myfile.tweets', 'r')
out_tweets = open('/home/thiago/Mestrado/topicos-BigData/Projeto-BigData/twitter-connection/selected.tweets', 'r')
'''
tweets_array = []
for i in tweets:
    tweet_json = json.loads(i)
    the_tweet = (tweet_json['id'], unidecode(tweet_json['text']), tweet_json['lang'])
    print the_tweet
    is_economics = raw_input()
    identification = (tweet_json['id'], unidecode(tweet_json['text']), tweet_json['lang'], is_economics)
    out_tweets.write(str(identification) + '\n')
    out_tweets.flush()

out_tweets.close()
'''
my_data = []
my_text_data = []
for i in out_tweets:
    splitted_row = i.split(',')
    d = dict(id=re.findall(r'\d+', splitted_row[0])[0],
             type=re.findall(r'\d+', splitted_row[len(splitted_row) - 1])[0],
             text=remove_http(''.join(splitted_row[1:len(splitted_row) - 2])))
    my_data.append(d)
    my_text_data.append(d['text'])

vectorizer = CountVectorizer(analyzer="word",
                             tokenizer=None,
                             preprocessor=None,
                             stop_words=None,
                             max_features=1500)

train_data = vectorizer.fit_transform(my_text_data)
train_data_features = train_data.toarray()

data_matrix = []
for i in range(485):
    data_list = (train_data_features[i], my_data[i]['type'])
    data_matrix.append(data_list)

for i in range(485, 500):
    res = knn(train_data_features[i], data_matrix, 'euclidian')
    print train_data_features[i], my_data[i]
    print res