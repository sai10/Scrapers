import urllib.request as urllib
from bs4 import BeautifulSoup
from datetime import datetime

y = 2006
years = []
while y <= datetime.now().year:
    years.append(str(y))
    y = y + 1


months = ['01','02','03','04','05','06','07','08','09','10','11','12']

fw = open('newsHindu.txt','w')

for yr in years:
    link = 'http://www.thehindu.com/archive/web/'
    link1 = link + yr + '/'
    print(link1)
    for mn in months:
        if int(mn) > datetime.now().month and int(yr) == datetime.now().year:
            break
        link2 = link1 +  mn + '/'
        print(link2)
        if mn == '02' and int(yr)%4==0:
            dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
        elif mn == '02':
            dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
        elif mn in ['01','03','05','07','08','10','12'] :
            dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        elif mn in ['04','06','09','11'] :
            dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        for dt in dates:
            if dt > datetime.now().day and int(mn) == datetime.now().month and int(yr) == datetime.now().year:
                break
            link3 = link2 + str(dt)
            print(link3)
            #fw.write(link3+'\n')
            link3 = urllib.Request(link3 , headers={'User-Agent' : "Magic Browser"})
            print(link3)
            page = urllib.urlopen(link3)
            soup = BeautifulSoup(page,'html.parser')
            for s in soup.findAll('div',attrs={'class':'section-container'}):
                for a in s.findAll('a'):
                    print(a.string)
                    news = a.string
                    if news != None:
                        fw.write(news.strip()+'\n')
