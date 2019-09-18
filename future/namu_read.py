import requests

BASE_ADDRESS = 'https://namu.wiki/w/'

with requests.Session() as s:
    keyword = input()

    ret = s.get(BASE_ADDRESS + keyword)

    print(ret.text)
