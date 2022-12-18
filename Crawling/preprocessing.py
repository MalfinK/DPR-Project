# preprocessing the crawled data

import re

def preprocessing(data) :
    # coversi emoticon
    emoticons = { 
        'Senang' : [':-)', ':)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}', ':^),' ':っ)'],
        'Ketawa' : [':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-', 'D', '=D', '=-3', '=3', 'B^D'],
        'Benci' : [':-||', ':@', '>:(',],
        'Kecewa' : [":$", ">:[", ":-(", ":(", ":-c", ":c", ":-<", ":っC", ":<", ":-[", ":[", ":{", ";(", ":'-(", ":'(", "D:<", "D:", "D8", "D;", "D=", "DX", "v.v", "D-':",],
        'Suka' : ['<3', ';-)', ';)', '-)', ')', ';-]', ';]', ';D', ';^)', ':-,'],
    }
    # replace emoticon
    for word in data:
        if word in emoticons['Senang']:
            data = data.replace(word, ' Senang ')
        elif word in emoticons['Ketawa']:
            data = data.replace(word, ' Ketawa ')
        elif word in emoticons['Benci']:
            data = data.replace(word, ' Benci ')
        elif word in emoticons['Kecewa']:
            data = data.replace(word, ' Kecewa ')
        elif word in emoticons['Suka']:
            data = data.replace(word, ' Suka ')
    # transform the crawled data to lower case
    data = data.lower()
    # remove all non-alphanumeric characters
    data = re.sub(r'[^a-z0-9\s]', '', data)
    # remove links
    data = re.sub(r'http\S+', '', data)
    # remove mentions
    data = re.sub(r'@\S+', '', data)
    # convert negation
    negation = ['kurang', 'tidak', 'enggak', 'ga', 'nggak', 'tak', 'gak']
    for i in range(len(data)):
        if i in negation:
            data = data.replace(word, word + '_' + word[i+1])
    # tokenize
    data = data.split()
    # filter tokens by length
    data = [word for word in data if len(word) > 1]
    # stopwords indonesia language
    stopwords = ['masih', 'Dong', 'Ke', 'Ada', 'Yoi', 'malam', 'Ya', 'Loe', 'Pada', 'Yang', 'Ini', 'Dan', 'Juga', 'Kita', 'Saya', 'untuk', 'Dari', 'Bagi', 'Iya', 'di', 'mana', 'kapan', 'Bisa', 'Mana', 'Itu', 'Sih', 'sudah', 'Bikin', 'dengan', 'Anda', 'Begitu','entah', 'Lalu', 'Yuk', 'Aku', 'Adalah', 'gue', 'Nanti', 'tunggu', 'Tau', 'Kemarin']
    # load stopwords
    # stopwords = open('stopwords.txt', 'r').read().split()
    # remove stopwords indonesia language
    data = [word for word in data if word not in stopwords]
    

    return data