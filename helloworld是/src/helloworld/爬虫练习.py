import urllib.request
from bs4 import BeautifulSoup
import json
"request = urllib.request(url)"
from test.test_urllib import urlopen
from test.test_decimal import file
movie = []
countw = 0
movies = []
url2 = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=1000&page_start=161"
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
req1=urllib.request.Request(url2) 
kkk1 = urllib.request.urlopen(req1,timeout=20)
soup1 = json.loads(kkk1.read())
wangye = soup1["subjects"]
for a in wangye:
    "movies.append(filter(str.isdigit, a[""]))"
    print( a["url"])
    count = 0
    while count<220:
        url = str(a["url"])+"comments?start="+str(count)+"&limit=20&sort=new_score&status=P"
        headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
        req=urllib.request.Request(url,headers=headers) 
        kkk = urllib.request.urlopen(req).read()
        count +=20
        movie.append(kkk)
        print(count)
    print('ok') 
    f= open("2.txt","a+",encoding='utf-8')
    countw+=1
    for kkk in movie:
        soup = BeautifulSoup(kkk,'html.parser',from_encoding = 'utf-8')
        tianna = soup.find_all("span",class_= "short") 
        for kkkk in tianna:
            fafafa = kkkk.get_text()
            f.write("\n"+"************************"+"\n") 
            f.write(fafafa)
            print("***************"+str(countw))