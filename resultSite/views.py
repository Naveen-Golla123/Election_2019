from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs
from .models import consistencyLS
from .models import consistencyAC
import logging

class News(object):
    cityblock=""
    img=""
    time=""
    link=""

class News_desc(object):
    p=[]
    heading="";
    time="";
    link="";



def mai(request):
    logger = logging.getLogger(__name__)
    allpack={}
    dist={1:"శ్రీకాకుళం జిల్లా",2:"విజయనగరం జిల్లా",3:"విశాఖపట్నం జిల్లా",4:"తూర్పు గోదావరి జిల్లా",5:"పశ్చిమ గోదావరి జిల్లా",6:"కృష్ణా జిల్లా",7:"గుంటూరు జిల్లా",8:"ప్రకాశం జిల్లా",9:"నెల్లూరు జిల్లా",10:"చిత్తూరు జిల్లా	",11:"కడప జిల్లా",12:"కర్నూలు జిల్లా",13:"అనంతపురం జిల్లా"}
    for i in range(1,14):
        picked=consistencyAC.objects.filter(district=i)
        allpack[dist[i]]=picked
    return render(request,"resultSite/index.html",{"allpack":allpack,"jsp":"Janasena Party","ycp":"Yuvajana Sramika Rythu Congress Party","tdp":"Telugu Desam"})





# """
#     for d in postman:
#
# """
def news(request):
    r=requests.get("https://telugu.oneindia.com/news/andhra-pradesh/");
    soup=bs(r.content,"html5lib");
    clearfixs=soup.findAll("li",attrs={'class':'clearfix'});
    fullpack={}
    count=0;
    for i in clearfixs:
        news=News();
        imgs=i.find("img")
        cityblock=i.find("div",attrs={'class':'cityblock-title'});
        fulllinks=i.find('a')
        time=i.find('div',attrs={'class':'cityblock-time'});
        if(imgs is not None and cityblock is not None and fulllinks is not None and time is not None):
            news.img=imgs.attrs['data-pagespeed-lazy-src'];
            news.cityblock=cityblock.text;
            news.link=fulllinks.attrs['href'];
            news.time=time.text;
            fullpack[count]=news;
            count=count+1;

    return render(request,"resultSite/news.html",{'fullpack':fullpack});


def news_desc(request):
    logger = logging.getLogger(__name__)
    URL="https://telugu.oneindia.com"+str(request.GET['YaLink']);
    # logger.warning(URL);
    news_desc=News_desc();
    r=requests.get(URL);
    soup=bs(r.content,"html5lib");
    news_desc.heading=soup.find('h1', attrs={"class":"heading"}).text;
    box=soup.find('div',attrs={'class':'oi-article-lt'});
    pa=box.findAll('p');
    for i in pa[:2]:
        news_desc.p.append(i.text);
    # imgdiv=soup.find('div',attrs={'class':'big_center_img'});
    # news_desc.img="https://telugu.oneindia.com"+str(imgdiv.find('img').attrs['data-pagespeed-lazy-src']);
    return render(request,"resultSite/news-desc.html",{'news_desc':news_desc});
