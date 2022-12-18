# preprocessing the crawled data

import re

def preprocessing(data) :
    # tokenisasi
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
    temp = []
    for word in data:
        # transform the crawled data to lower case
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
        if data[i] != data[len(data) - 1]:
            if data[i] in negation:
                data[i] = data[i] + '_' + data[i+1]
                data[i+1] = ''
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
    # stemming
    for i in range(len(data)):
        # word endwith
        if data[i].endswith('nya') or data[i].endswith('kah') or data[i].endswith('lah') or data[i].endswith('pun') or data[i].endswith('kan'):
            data[i] = data[i][:-3]
        elif data[i].endswith('ku') or data[i].endswith('mu'):
            data[i] = data[i][:-2]
        elif data[i].endswith('i'):
            data[i] = data[i][:-1]
        # word startwith
        if data[i].startswith('mem') or data[i].startswith('kan') or data[i].startswith('ter') or data[i].startswith('ber') or data[i].startswith('bel') or data[i].startswith('per') or data[i].startswith('pel'):
            data[i] = data[i][3:]
        elif data[i].startswith('me') or data[i].startswith('di') or data[i].startswith('ke') or data[i].startswith('se'):
            data[i] = data[i][2:]
        elif data[i].startswith('m'):
            data[i] = data[i][1:]
    return data