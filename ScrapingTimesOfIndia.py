import urllib.request as urllib
from bs4 import BeautifulSoup
from datetime import datetime

y = 2001
years = []
while y <= datetime.now().year:
    years.append(str(y))
    y = y + 1

#years = ['2017']

months = ['1','2','3','4','5','6','7','8','9','10','11','12']

fw = open('timesofindia.txt','w')
starttime = 36892

#starttime = 43009
for yr in years:
    link = 'https://timesofindia.indiatimes.com/'
    link1 = link +yr+'/'
    print(link1)
    for mn in months:
        if int(mn) > datetime.now().month and int(yr) == datetime.now().year:
            break
        link2 = link1 + mn + '/'
        if mn == '2' and int(yr)%4==0:
            dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
        elif mn == '2':
            dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
        elif mn in ['1','3','5','7','8','10','12'] :
            dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        elif mn in ['4','6','9','11'] :
            dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        for dt in dates:
            if dt > datetime.now().day and int(mn) == datetime.now().month and int(yr) == datetime.now().year:
                break
            link3 = link2 + str(dt) + '/archivelist/year-'+yr+',month-'+mn+',starttime-'+str(starttime)+'.cms'
            print(link3)
            reqlink = urllib.Request(link3)
            page = urllib.urlopen(reqlink)
            soup = BeautifulSoup(page,'html.parser')
            #fw.write(link3+'\n')
            for td in soup.findAll('td'):
                for s in td.findAll('span',recursive=False):
                    for a in s.findAll('a'):
                        print(a.string)
                        news = a.string
                        if news != None:
                            fw.write(news+'\n')
            starttime += 1

