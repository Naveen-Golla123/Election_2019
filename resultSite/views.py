from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs
from .models import consistencyLS
from .models import consistencyAC
import logging

# Create your views here.
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
