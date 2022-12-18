# preprocessing the crawled data

import re


def preprocessing(data) :
    # transform the crawled data to lower case
    data = data.lower()
    # remove all non-alphanumeric characters
    data = re.sub(r'[^a-z0-9\s]', '', data)
    # remove links
    data = re.sub(r'http\S+', '', data)
    # remove mentions
    data = re.sub(r'@\S+', '', data)
    # tokenize
    data = data.split()
    # filter tokens by length
    data = [word for word in data if len(word) > 4]
    # stopwords indonesia language
    stopwords = ['yang', 'dari', 'dengan', 'kepada', 'untuk', 'adalah', 'sebagai', 'pada', 'dalam', 'sebuah', 'seorang', 'sejak', 'sampai', 'sebelum', 'sesudah', 'sementara', 'sehingga', 'sekalipun', 'sebagaimana', 'sebagainya', 'sebaik', 'sebaiknya', 'sebaliknya', 'sebanyak', 'sebegini', 'sebegitu', 'sebelumnya', 'sebenarnya', 'seberapa', 'sebesar', 'sebetulnya', 'sebisanya', 'sebuah', 'sebut', 'sebutlah', 'sebutnya', 'secara', 'secukupnya', 'sedang', 'sedangkan', 'sedemikian', 'sedikit', 'sedikitnya', 'seenaknya', 'segala', 'segalanya', 'segera', 'seharusnya', 'sehingga', 'seingat', 'sejak', 'sejenak', 'sejumlah', 'sekadar', 'sekadarnya', 'sekali', 'sekali-kali', 'sekalian', 'sekaligus', 'sekalipun', 'sekarang', 'sekarang', 'sekecil', 'seketika', 'sekiranya', 'sekitar', 'sekitarnya', 'sekurang-kurangnya', 'sekurangnya', 'sela', 'selain', 'selaku', 'selalu', 'selama', 'selama-lamanya', 'selamanya', 'selanjutnya', 'seluruh', 'seluruhnya', 'semacam', 'semakin', 'semampu', 'semampunya', 'semasa', 'semasih', 'semata', 'semata-mata', 'semaunya', 'sementara', 'semisal', 'semisalnya', 'sempat', 'semua', 'semuanya', 'semula', 'sendiri', 'sendirian', 'sendirinya', 'seolah', 'seolah-olah', 'seorang', 'sepanjang', 'sepantasnya', 'sepantasnyalah', 'seperlunya', 'seperti', 'sepertinya', 'sepihak', 'sering', 'seringnya', 'serta', 'serupa', 'sesaat', 'sesama', 'sesampai', 'sesegera', 'sesekali', 'seseorang', 'sesuatu', 'sesuatunya', 'sesudah', 'sesudahnya', 'setelah', 'setempat', 'setengah', 'seterusnya', 'setiap', 'setiba', 'setibanya', 'setidak-tidaknya', 'setidaknya', 'seting']
    # load stopwords
    # stopwords = open('stopwords.txt', 'r').read().split()
    # remove stopwords indonesia language
    data = [word for word in data if word not in stopwords]

    return data