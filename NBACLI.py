from bs4 import BeautifulSoup

import requests

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
print("--------------")
for x in range(0,len(filteredteams)-1):
    if (x % 2 == 0):
        print(filteredteams[x] + ": " + filteredscores[x])
        print(filteredteams[x+1] + ": " + filteredscores[x+1])
        print("--------------")






