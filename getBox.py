from config import *
from bs4 import BeautifulSoup
import requests

def getBox():
    r = requests.get("http://stats.nesn.com/nba/boxscore.asp?gamecode=2017122311&home=11&vis=17")
    soup = BeautifulSoup(r.text,'lxml')

    for h in soup.find_all("tr","shsRow0Row"):
        players0.append(h)

    for h in soup.find_all("tr","shsRow1Row"):
        players1.append(h)

    for h in players0:
        for j in h.find_all("td","shsTotD"):
            data0.append(j.string)

    for h in players1:
        for j in h.find_all("td","shsTotD"):
            data1.append(j.string)

    for h in soup.find_all("a"):
        if (str(h.string)[1] == "."):
            players.append(str(h.string))

    print(players)
    
