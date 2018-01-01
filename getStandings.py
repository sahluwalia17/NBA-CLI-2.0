from config import *
from bs4 import BeautifulSoup
import requests

def getStandings():
    r = requests.get("http://stats.nesn.com/nba/standings_conference.asp")
    soup = BeautifulSoup(r.text,"lxml")

    for a in soup.find_all("a"):
        sTeams.append(str(a))

    for a in sTeams:
        if "teamhome" in a:
            b = str(a)[:-1]
            x = b.rindex(">") + 1
            filteredsTeams.append(b[x:len(b) - 3])
            
    for a in soup.find_all("td","shsTotD"):
        teamRecords.append(a.string)

    for a in teamRecords:
        if a.isdigit() == True:
            filteredteamRecords.append(a)
            
