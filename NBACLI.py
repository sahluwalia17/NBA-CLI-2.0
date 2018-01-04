from config import *
from getGames import *
from getBox import *
from getUpcoming import *
from getStandings import *
from cmd2 import Cmd, make_option, options
import requests

class NBACLI(Cmd):
    Cmd.prompt="NBA> "

    def do_games(self,arg,opts=None):
        print("Current NBA games being played/Games that have finished:")
        
        #storing information in config files by calling getGames/getUpcoming script
        getGames()
        getUpcoming()
        new = [x for x in upcoming if x not in filteredteams]
        
        #teams playing formatting
        if (len(filteredteams) > 0):
            print("------------------")
            for x in range(0,len(filteredteams)-1):
                if (x % 2 == 0):
                    a = int(x / 2)
                    firstadjust1 = len(filteredteams[x]+":")
                    firstadjust2 = len(filteredscores[x])
                    secondadjust1 = len(filteredteams[x+1]+":")
                    secondadjust2 = len(filteredscores[x+1])
                    statusL = len("Status: " + status[a])
                    print("Status: " + status[a].rjust(18-statusL + 5))
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
            print("No games have begun yet! Checking for upcoming games...")
            for x in range(0,len(new)-1):
                if (x % 2 == 0):
                    a = int(x/2)
                    print(new[x] + " vs. " + new[x+1] + " at " + upcomingTimes[a] + ".")

        if len(filteredteams) > 0 and len(new) > 0:
            print()
            print("Checking for upcoming games...")
            for x in range(0,len(new)-1):
                if (x % 2 == 0):
                    a = int(x/2)
                    print(new[x] + " vs. " + new[x+1] + " at " + upcomingTimes[a] + ".")
            
        
        print()
        
    def do_standings(self,arg,opts = None):
        #storing information in config files by calling get Standings script
        getStandings()

        counter = 1
        #standings formatting
        for x in range(0,len(filteredsTeams)):
            if x == 0:
                print("Eastern Conference Standings")
            if x == 15:
                counter = 1
                print()
                print("Western Conference Standings")
            a = x * 2
            if counter < 10:
                print(str(counter) + ".  " + filteredsTeams[x] + ": " + filteredteamRecords[a] + " - " + filteredteamRecords[a+1])
            if counter >= 10:
                print(str(counter) + ". " + filteredsTeams[x] + ": " + filteredteamRecords[a] + " - " + filteredteamRecords[a+1])

            counter = counter + 1
        print()

    def do_test(self,arg,opts=None):
        getBox()

nba = NBACLI()
nba.cmdloop()






