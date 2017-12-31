from config import *
from getGames import *
from getBox import *
from getUpcoming import *
import requests

print("Current NBA games being played!")

#storing information in config files by calling getGames script
getGames()

#teams playing formatting
if (len(filteredteams) > 0):
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
    
if (len(filteredteams) == 0):
    print()
    print("No games currently being played! Checking for upcoming games...")
    getUpcoming()

getBox()

input()






