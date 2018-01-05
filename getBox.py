from config import *
from bs4 import BeautifulSoup
from collections import OrderedDict
import requests

def getBox():
    r = requests.get("http://stats.nesn.com/nba/boxscore.asp?gamecode=2018010410&home=10&vis=9")
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

    filteredplayers = [x for x in filteredplayers if x not in DNP]
    check = False
    
    #this is checking for play by play
    if ":" in str(stats[0]) and ":" in str(stats[1]):
        stats = stats[11:]
    
    #boxScores outputting
    for x in range(0,len(filteredplayers)):
        if check == False:
            a = x * 14
            
        if stats[a] != "\xa0" and check == False:
            a = x * 14
            print(filteredplayers[x] + " | Minutes: " + str(stats[a+1]) + " | FGM - FGA: " + str(stats[a+2]) + " | FTM - FTA: " + str(stats[a+3]) + " | 3PM - 3PA: " + str(stats[a+4]) + " | Rebounds: " + str(stats[a+7]) + " | Assists: " + str(stats[a+8]) + " | Blocks: " + str(stats[a+9]) + " | Steals: " + str(stats[a+10]) + " | Turnovers: " + str(stats[a+11]) + " | Points: " + str(stats[a+13]))
            print()
            pass
            
        if (stats[a] == "\xa0" and check == False):
            check = True
            print("Totals: " + " | Minutes: " + str(stats[a+1]) + " | Rebounds: " + str(stats[a+7]) + " | Assists: " + str(stats[a+8]) + " | Blocks: " + str(stats[a+9]) + " | Steals: " + str(stats[a+10]) + " | Turnovers: " + str(stats[a+11]) + " | Points: " + str(stats[a+13]))
            print()
            a = (x+1) * 14
            print(filteredplayers[x] + " | Minutes: " + str(stats[a+1]) + " | FGM - FGA: " + str(stats[a+2]) + " | FTM - FTA: " + str(stats[a+3]) + " | 3PM - 3PA: " + str(stats[a+4]) + " | Rebounds: " + str(stats[a+7]) + " | Assists: " + str(stats[a+8]) + " | Blocks: " + str(stats[a+9]) + " | Steals: " + str(stats[a+10]) + " | Turnovers: " + str(stats[a+11]) + " | Points: " + str(stats[a+13]))
            print()
            pass

        if check == True and stats[a] != "\xa0":
            a = (x+1) * 14
            print(filteredplayers[x] + " | Minutes: " + str(stats[a+1]) + " | FGM - FGA: " + str(stats[a+2]) + " | FTM - FTA: " + str(stats[a+3]) + " | 3PM - 3PA: " + str(stats[a+4]) + " | Rebounds: " + str(stats[a+7]) + " | Assists: " + str(stats[a+8]) + " | Blocks: " + str(stats[a+9]) + " | Steals: " + str(stats[a+10]) + " | Turnovers: " + str(stats[a+11]) + " | Points: " + str(stats[a+13]))
            print()
            pass

        if check == True and stats[a] == "\xa0":
            a = (x+1) * 14
            print("Totals: " + " | Minutes: " + str(stats[a+1]) + " | Rebounds: " + str(stats[a+7]) + " | Assists: " + str(stats[a+8]) + " | Blocks: " + str(stats[a+9]) + " | Steals: " + str(stats[a+10]) + " | Turnovers: " + str(stats[a+11]) + " | Points: " + str(stats[a+13]))
            print()
    
