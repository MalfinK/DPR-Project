import tweepy
import re

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAO3%2BigEAAAAAap1frk%2FV1bDMLWcNs5IdcoE%2FEb4%3D1kg0iclHuoXmPc8ZL18xdYOyNOMnQ1WjbgUiLSx5sNGW0kGxN0'

client = tweepy.Client(bearer_token)
# kata_kunci = 'ga_seru'
# respon_data = client.search_recent_tweets(kata_kunci, max_results=100)
# print(respon_data)

key = ['MATA NAJWA', 'Stand Up Comedy', 'indonesia idol', '@OVJ_Trans7', 'YKS', '@WCIndonesia', 'Rising Star Indonesia', 'ILK (Indonesia lawak klub)']

with open("hasil_crawler.txt", "w", encoding="utf8") as hasilKeseluruhan:
    for tags in key:
        # print("KEY => PROGRAM TV", file=hasilKeseluruhan)
        data = client.search_recent_tweets(query=tags, max_results=100)
        # print(data)
        for tweet in data.data:
            hasilBanyakKata = re.sub(
                pattern="[^\w\s]",
                repl="",
                string=tweet.text)
            hasilBanyakKata = hasilBanyakKata.lower()
            # print('-----------------------------', file=hasilKeseluruhan)
            # print("Penanda Tweet Seseorang Start", file=hasilKeseluruhan)
            # print('-----------------------------', file=hasilKeseluruhan)
            print(hasilBanyakKata, file=hasilKeseluruhan)
            # print('----------------------------', file=hasilKeseluruhan)
            # print("Penanda Tweet Seseorang Stop", file=hasilKeseluruhan)
            # print('----------------------------\n\n', file=hasilKeseluruhan)
            print('\n', file=hasilKeseluruhan)
