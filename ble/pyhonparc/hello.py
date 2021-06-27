import requests
from bs4 import BeautifulSoup

#headers - 코드단에서 요청할 때 기본적으로 막아둔 사이트들이 많아서 브라우저에서 엔터친 것 마냥 하도록 하는 것
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
#크롤링이 가능한 기본적 이유는? 인터넷과 관계 없음. 이미 받아온 걸 가지고(requersts) 내가 솟아내는게 크롤링(ba4)

#기술적 2가지 필요
#1. 코드단에서 요청을 하는 것 - requersts
#2. html중에 내에서 html을 솟아내는 것  - ba4

#db사용
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

trslist = soup.select('#old_content > table > tbody > tr')

for tr in trslist:
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        star = tr.select_one('td.point').text
        doc = {
            'rank':rank,
            'title':title,
            'star':star
        }
        db.movies.insert_one(doc)


