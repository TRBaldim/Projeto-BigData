import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier


def review_to_words(raw_review):
    # Remove the HTML
    review_text = BeautifulSoup(raw_review, 'lxml').get_text()
    # Get only letters
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    # Converto to vector of words
    words = letters_only.lower().split()
    # Get the dataset of stopwords in english
    stops = set(stopwords.words("english"))
    # Reading data
    mean_words = [w for w in words if not w in stops]
    return " ".join(mean_words)


train = pd.read_csv("../datasets/labeledTrainData.tsv",
                    header=0,
                    delimiter='\t',
                    quoting=3)
'''
test = pd.read_csv("../datasets/testData.tsv",
                   header=0,
                   delimiter='\t',
                   quoting=3)
'''


num_of_reviews = len(train['review'])
text_data = []
for i in xrange(0, num_of_reviews):
    if (i + 1) % 1000 == 0:
        print "Review %d of %d\n" % (i+1, num_of_reviews)
    text_data.append(review_to_words(train['review'][i]))

vectorizer = CountVectorizer(analyzer="word",
                             tokenizer=None,
                             preprocessor=None,
                             stop_words=None,
                             max_features=5000)

train_data = vectorizer.fit_transform(text_data[:20000])

train_data_features = train_data.toarray()

print len(train_data_features)
print len(train_data_features[0])

'''
vocab = vectorizer.get_feature_names()

forest = RandomForestClassifier(n_estimators=100)
df = train
train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)
forest = forest.fit(train_data_features, train['sentiment'])

num_of_reviews = len(test['review'])
clean_test_review = []

for i in xrange(0, num_of_reviews):
    if(i+1) % 1000 == 0:
        print "Review %d of %d\n" % (i+1, num_of_reviews)
    clean_review = review_to_words(test["review"][i])
    clean_test_review.append(clean_review)


test_data_features = vectorizer.transform(test['review'])
test_data_features = test_data_features.toarray()

result = forest.predict(test_data_features)

output = pd.DataFrame(data={'id': test['id'], 'sentiment': result})

for i in output.toarray():
    print i
'''