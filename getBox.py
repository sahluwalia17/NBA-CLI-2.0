from config import *
from bs4 import BeautifulSoup
from collections import OrderedDict
import requests

def getBox():
    r = requests.get("http://stats.nesn.com/nba/boxscore.asp?gamecode=2018010320&home=20&vis=24&final=true")
    soup = BeautifulSoup(r.text,'lxml')
    #print(soup)
    
    players = []
    DNP = []
    stats = []

    for h in soup.find_all("tr"):
        for a in h.find_all("td"):
            rawdata.append(a)
            
    for a in rawdata:
        for h in a.find_all("a"):
            if (str(h.string)[1] == "." or str(h.string) == "Nene"):
                players.append(str(h.string))

    #have to remove players who have extra information associated with them such as Technicals because it causes them to appear twice in the players list
    filteredplayers = list(dict.fromkeys(players).keys())

    for h in soup.find_all("td", "shsDNP"):
        if (str(h.string)[1] == "."):
            DNP.append(h.string)
    
    for h in soup.find_all("td","shsTotD"):
        stats.append(h.string)
        
    stats = stats[17:]
    print(stats)
            
    
