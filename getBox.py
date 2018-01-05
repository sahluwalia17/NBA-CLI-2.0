from config import *
from bs4 import BeautifulSoup
from collections import OrderedDict
import requests

def getBox(gid):
    #r = requests.get(filteredurls[gid-1])
    r = requests.get("http://stats.nesn.com/nba/boxscore.asp?gamecode=2018010412&home=12&vis=25&final=true")
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
    team = (gid-1) * 2

    puts(colored.magenta(filteredteams[team] + " BoxScore"))
    puts(colored.magenta("--------------------------------"))
    for x in range(0,len(filteredplayers)):
        if check == False:
            a = x * 14
            
        if stats[a] != "\xa0" and check == False:
            a = x * 14
            puts(colored.cyan(filteredplayers[x] + " | M: " + str(stats[a+1]) + " | FGM - FGA: " + str(stats[a+2]) + " | FTM - FTA: " + str(stats[a+3]) + " | 3PM - 3PA: " + str(stats[a+4]) + " | R: " + str(stats[a+7]) + " | A: " + str(stats[a+8]) + " | B: " + str(stats[a+9]) + " | S: " + str(stats[a+10]) + " | T: " + str(stats[a+11]) + " | P: " + str(stats[a+13])))
            print()
            pass
            
        if (stats[a] == "\xa0" and check == False):
            check = True
            puts(colored.cyan("Totals: " + " | M: " + str(stats[a+1]) + " | R: " + str(stats[a+7]) + " | A: " + str(stats[a+8]) + " | B: " + str(stats[a+9]) + " | S: " + str(stats[a+10]) + " | T: " + str(stats[a+11]) + " | P: " + str(stats[a+13])))
            print()
            puts(colored.magenta(filteredteams[team+1] + " Boxscore"))
            puts(colored.magenta("--------------------------------"))

            a = (x+1) * 14
            puts(colored.yellow(filteredplayers[x] + " | M: " + str(stats[a+1]) + " | FGM - FGA: " + str(stats[a+2]) + " | FTM - FTA: " + str(stats[a+3]) + " | 3PM - 3PA: " + str(stats[a+4]) + " | R: " + str(stats[a+7]) + " | A: " + str(stats[a+8]) + " | B: " + str(stats[a+9]) + " | S: " + str(stats[a+10]) + " | T: " + str(stats[a+11]) + " | P: " + str(stats[a+13])))
            print()
            pass

        if check == True and stats[a] != "\xa0":
            a = (x+1) * 14
            puts(colored.yellow(filteredplayers[x] + " | M: " + str(stats[a+1]) + " | FGM - FGA: " + str(stats[a+2]) + " | FTM - FTA: " + str(stats[a+3]) + " | 3PM - 3PA: " + str(stats[a+4]) + " | R: " + str(stats[a+7]) + " | A: " + str(stats[a+8]) + " | B: " + str(stats[a+9]) + " | S: " + str(stats[a+10]) + " | T: " + str(stats[a+11]) + " | P: " + str(stats[a+13])))
            print()
            pass

        if check == True and stats[a] == "\xa0":
            a = (x+1) * 14
            puts(colored.yellow("Totals: " + " | M: " + str(stats[a+1]) + " | R: " + str(stats[a+7]) + " | A: " + str(stats[a+8]) + " | B: " + str(stats[a+9]) + " | S: " + str(stats[a+10]) + " | T: " + str(stats[a+11]) + " | P: " + str(stats[a+13])))
            print()
    
