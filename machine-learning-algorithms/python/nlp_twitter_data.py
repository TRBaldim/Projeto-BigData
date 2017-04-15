from algorithms import knn
import re
import json
from unidecode import unidecode
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import matplotlib as mlt

mlt.use('TkAgg')

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
for i in range(460):
    data_list = (train_data_features[i], my_data[i]['type'])
    data_matrix.append(data_list)

dict_data = {}
for type in ['euclidian', 'quadratic', 'cos']:
    print type
    ks = []
    acc = []
    to_pandas = {}
    for k in range(1, 21):
        positive = 0
        count_data = 0
        for i in range(460, 500):
            res = knn(train_data_features[i], data_matrix, type, k=k)
            if my_data[i]['type'] == res:
                positive += 1
            count_data += 1
        print k, float(positive)/float(count_data)
        ks.append(k)
        acc.append(float(positive)/float(count_data))
    to_pandas['k'] = ks
    to_pandas['accuracy'] = acc
    dict_data[type] = pd.DataFrame(to_pandas)

plt.plot(dict_data['euclidian']['k'], dict_data['euclidian']['accuracy'], label='Euclidian')
plt.plot(dict_data['quadratic']['k'], dict_data['quadratic']['accuracy'], label='Quadratic')
plt.plot(dict_data['cos']['k'], dict_data['cos']['accuracy'], label='Cosine')
plt.ylabel('Accuracy')
plt.xlabel('KNN')
#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#           ncol=2, mode="expand", borderaxespad=0.)
plt.show()


