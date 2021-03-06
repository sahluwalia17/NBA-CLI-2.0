from config import *
from bs4 import BeautifulSoup
import requests



def getGames():
    r = requests.get("http://stats.nesn.com/nba/scoreboard.asp?meta=true")
    soup = BeautifulSoup(r.text,'lxml')

    #Finding teams that played
    for h in soup.find_all("td", "shsLeaderTtl"):
        teams.append(h.string)

    for x in range(0,len(teams)):
        if (x % 3 != 0):
            filteredteams.append(teams[x])
        
    #Finding total scores for each team
    for h in soup.find_all("td", "shsTotD"):
        scores.append(h.string)
    
    for h in range (0,len(scores)):
        if (scores[h] == "Tot"):
            filteredscores.append(scores[h+5])
            filteredscores.append(scores[h+10])
            
    for h in soup.find_all("td","shsTeamCol shsNamD"):
        status.append(h.string)

    #retrieving box score urls

    for h in soup.find_all("td","shsLiveNav"):
        for a in h.find_all("a",href = True):
            urls.append(str(a["href"]))

    for h in urls:
        if "preview" not in h and "recap" not in h:
            filteredurls.append("http://stats.nesn.com" + h)

    
#Sahil Ahluwalia 2018
    
