# preprocessing of the data

import re
import string

def preprocessing(data):
    # lowercase
    data = data.lower()
    # remove numbers
    data = re.sub(r'\d+', '', data)
    # remove punctuation
    data = data.translate(str.maketrans('', '', string.punctuation))
    # remove whitespace leading & trailing
    data = data.strip()
    # remove multiple whitespace into single whitespace
    data = re.sub('\s+', ' ', data).strip()
    # tokenizing
    data = data.split()
    # stopping word
    with open('crawler_ending.txt', 'r', encoding='utf-8') as f:
        stopwords = f.read()
        stopwords = stopwords.split()
    data = [word for word in data if word not in stopwords]
    # stemming
    with open('crawler_stemming.txt', 'r', encoding='utf-8') as f:
        stemming = f.read()
        stemming = stemming.split()
    for index, word in enumerate(data):
        for stem in stemming:
            if word in stem:
                data[index] = stem.split(':')[0]
    # return ' '.join(data)
    return data

with open('hasil.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    data = preprocessing(data)
    print(data + '\n', file=open('hasil_preprocessing.txt', 'w', encoding='utf-8'))