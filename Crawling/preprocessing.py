# preprocessing the crawled data

import re

def preprocessing(data) :
    data = data.split()
    # coversi emoticon
    emoticons = { 
        'senang' : [':-)', ':)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}', ':^),' ':っ)', '😁'],
        'ketawa' : [':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-', 'D', '=D', '=-3', '=3', 'B^D', '🤣', '😂'],
        'benci' : [':-||', ':@', '>:('],
        'kecewa' : [":$", ">:[", ":-(", ":(", ":-c", ":c", ":-<", ":っC", ":<", ":-[", ":[", ":{", ";(", ":'-(", ":'(", "D:<", "D:", "D8", "D;", "D=", "DX", "v.v", "D-':", '😌'],
        'suka' : ['<3', ';-)', ';)', '-)', ')', ';-]', ';]', ';D', ';^)', ':-,', '🥰'],
    }
    # replace emoticon
    for i in range(len(data)):
        if data[i] in emoticons['senang']:
            data[i] = 'senang'
        elif data[i] in emoticons['ketawa']:
            data[i] = 'ketawa'
        elif data[i] in emoticons['benci']:
            data[i] = 'benci'
        elif data[i] in emoticons['kecewa']:
            data[i] = 'kecewa'
        elif data[i] in emoticons['suka']:
            data[i] = 'suka'
            
    # transform the crawled data to lower case
    temp = []
    for word in data:
        word = word.lower()
        # remove all non-alphanumeric characters
        word = re.sub(r'[^a-z0-9\s]', '', word)
        # remove links
        word = re.sub(r'http\S+', '', word)
        # remove mentions
        word = re.sub(r'@\S+', '', word)
        temp.append(word)
    data = temp
    # convert negation
    negation = ['kurang', 'tidak', 'enggak', 'ga', 'nggak', 'tak', 'gak']
    for i in range(len(data)):
        if data[i] in negation:
            data[i] = data[i] + '_' + data[i+1]
    # # tokenize
    # data = data.split()
    # filter tokens by length
    data = [word for word in data if len(word) > 1]
    # stopwords indonesia language
    stopwords = ['masih', 'Dong', 'Ke', 'Ada', 'Yoi', 'malam', 'Ya', 'Loe', 'Pada', 'Yang', 'Ini', 'Dan', 'Juga', 'Kita', 'Saya', 'untuk', 'Dari', 'Bagi', 'Iya', 'di', 'mana', 'kapan', 'Bisa', 'Mana', 'Itu', 'Sih', 'sudah', 'Bikin', 'dengan', 'Anda', 'Begitu','entah', 'Lalu', 'Yuk', 'Aku', 'Adalah', 'gue', 'Nanti', 'tunggu', 'Tau', 'Kemarin']
    # load stopwords
    # stopwords = open('stopwords.txt', 'r').read().split()
    # remove stopwords indonesia language
    data = [word for word in data if word not in stopwords]
    

    return data