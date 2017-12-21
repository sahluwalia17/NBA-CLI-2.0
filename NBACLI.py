from bs4 import BeautifulSoup

import requests

print("Current NBA games being played!")
print()

#containers
teams = []
filteredteams = []
scores = []
filteredscores = []


r = requests.get("http://stats.nesn.com/nba/scoreboard.asp")
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

#teams playing formatting
print("------------------")
for x in range(0,len(filteredteams)-1):
    if (x % 2 == 0):
        firstadjust1 = len(filteredteams[x]+":")
        firstadjust2 = len(filteredscores[x])
        secondadjust1 = len(filteredteams[x+1]+":")
        secondadjust2 = len(filteredscores[x+1])
        if(firstadjust2 == 2):
            print(filteredteams[x] + ": " + filteredscores[x].rjust(18 - firstadjust1 - firstadjust2 + 1))
        if(firstadjust2 == 3):
            print(filteredteams[x] + ": " + filteredscores[x].rjust(18 - firstadjust1 - firstadjust2 + 2))
        if(secondadjust2 == 2):
            print(filteredteams[x+1] + ": " + filteredscores[x+1].rjust(18 - secondadjust1 - secondadjust2 + 1))
        if(secondadjust2 == 3):
            print(filteredteams[x+1] + ": " + filteredscores[x+1].rjust(18 - secondadjust1 - secondadjust2 + 2))
        print("------------------")






