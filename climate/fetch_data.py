import requests
from django.shortcuts import get_object_or_404
from .models import *
import requests
from bs4 import BeautifulSoup
import threading

class storedata:
    def __init__(self,Model,country='',y='',jan='',feb='',mar='',apr='',may='',jun='',jul='',aug='',sep='',octo='',nov='',dec=''):
        self.ModelName=Model
        temp_obj=self.ModelName(country=country,jan=jan,feb=feb, mar=mar, apr=apr,
                                                            may=may, jun=jun, jul=jul, aug=aug,
                                                            sep=sep, octo=octo,nov=nov, dec=dec,year=y)
        temp_obj.save()

#function for storing datat to database
def rec(self,ModelName,path):
    self.path=path
    self.ModelName=ModelName
    ls=[]
    l=[]
    month=''
    country=''
    pk=''
    tc=0
    mc=1
    # yc=1
    cnt=0
    # def store_record(request):

    res=requests.get(self.path)
    file=list((res.text).split('\r\n'))

    for i in file:
        print(i)
        print('-'*100)
        sub_list=list((i).split())
        print(sub_list)
        if len(sub_list)>0:
            ls.append(sub_list)
    country=ls[0][0]


    if Country.objects.filter(name__iexact=country).count()==1:
        pass
    else:
        obj=Country(name=country)
        obj.save()
    contry_obj=get_object_or_404(Country,name=country)

    for j in ls[7:]:

        if len(j)>=13:#new
            y=j[0]
            jan=j[1]
            feb=j[2]
            mar=j[3]
            apr=j[4]
            may=j[5]
            jun=j[6]
            jul=j[7]
            aug=j[8]
            sep=j[9]
            octo=j[10]
            nov=j[11]
            dec=j[12]

        if self.ModelName.objects.filter(country=contry_obj,jan=jan, feb=feb, mar=mar, apr=apr,
                                                            may=may, jun=jun, jul=jul, aug=aug,
                                                            sep=sep, octo=octo,nov=nov, dec=dec,year=y).count()==1:
                                                            pass



        else:
            s=storedata(self.ModelName,contry_obj,y,jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec)
            cnt=cnt+1
            print(cnt)


    print('Done')

def scrap_data(self):
    r= requests.get('https://www.metoffice.gov.uk/climate/uk/summaries/datasets#yearOrdered')
    soup=BeautifulSoup(r.content,"html.parser")
    data=soup.find_all("a",{"class":"external"})
    l=[]
    lmin=[]
    lmax=[]
    lmean=[]
    lsun=[]
    lrain=[]
    for x in data:
        d=x.get('href')
        l.append(d)

    #generate list for Min,Max,Mean,Sunshine and Rainfall
    for j in l:
        if 'Tmin/date' in j:
            lmin.append(j)
        if 'Tmax/date' in j:
            lmax.append(j)
        if 'Tmean/date' in j:
            lmean.append(j)
        if 'Sunshine/date' in j:
            lsun.append(j)
        if 'Rainfall/date' in j:
            lrain.append(j)

    #store data in database by calling 'rec' function
    for path in lmin[:5]:
        rec(self,MinTemp,path)
    for path in lmax[:5]:
        rec(self,MaxTemp,path)
    for path in lmean[:5]:
        rec(self,MeanTemp,path)
    for path in lsun[:5]:
        rec(self,Sunshine,path)
    for path in lrain[:5]:
        rec(self,Rainfall,path)
