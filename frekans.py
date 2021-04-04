import urllib.request
from bs4 import BeautifulSoup
def adetbul(veriler):
    for i in veriler:    
        print(i,"adet: ",veriler.count(i))
def semboltemizle(tumkelimeler):
    sembolsuzkelimeler=[]
    semboller="!'^+%&/()=?_£#${[]}\,<>."+chr(775)
    for kelime in tumkelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime=kelime.replace(sembol,"")
        if(len(kelime)>0):
           sembolsuzkelimeler.append(kelime)
    return sembolsuzkelimeler
site="https://www.ntv.com.tr/turkiye/son-dakika-haberi-ak-parti-mhp-ittifakinda-yarin-liderlere-sunum-yapilacak,qzUvQBVoTU-zdmVJ5eSH8w"
tumkelimeler=[]
veri=urllib.request.urlopen(site)
soup=BeautifulSoup(veri,"html.parser")
for kelimegrupları in soup.find_all("p"):
    icerik=kelimegrupları.text
    kelimeler=icerik.lower().split()
    for kelime in kelimeler:
        tumkelimeler.append(kelime)
       
    
    
tumkelime=semboltemizle(tumkelimeler)
for i in tumkelime:
    print(i)
adetbul(tumkelime)