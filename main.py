import json
import os
from top_tweets import top_tweets

def main ():
    #top_tweets(path)
    print('hola0')
    with open('farmers-protest-tweets-2021-03-5.json', 'r') as file:
        print('hola')
        data = json.load(file)
        print('hola2')
        for i in data["url"]:
            print(i)
main()