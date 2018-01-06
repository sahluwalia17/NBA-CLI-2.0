from config import *
from bs4 import BeautifulSoup
import requests

def getUpcoming():
    r = requests.get("http://stats.nesn.com/nba/scoreboard.asp?meta=true")
    soup = BeautifulSoup(r.text,'lxml')

    #getting the games to be played
    for a in soup.find_all("td","shsNamD"):
        for b in a.find_all("a"):
            upcoming.append(str(b.string))

    #getting the times for games to be played
    for a in soup.find_all("span", class_ = "shsTimezone shsETZone"):
        upcomingTimes.append(str(a.string))

#Sahil Ahluwalia 2018
