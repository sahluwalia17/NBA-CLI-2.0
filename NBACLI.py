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
        print("Current NBA games being played:")
        
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
            for x in range(0,len(upcoming)-1):
                if (x % 2 == 0):
                    a = int(x/2)
                    print(upcoming[x] + " vs. " + upcoming[x+1] + " at " + upcomingTimes[a] + ".")
        print()
        
    def do_standings(self,arg,opts = None):
        #storing information in config files by calling get Standings script
        getStandings()

        #standings formatting
        for x in range(0,len(filteredsTeams)):
            if x == 0:
                print("Eastern Conference Standings")
            if x == 15:
                print()
                print("Western Conference Standings")
            a = x * 2
            print(filteredsTeams[x] + ": " + filteredteamRecords[a] + " - " + filteredteamRecords[a+1])
        print()

    def do_test(self,arg,opts=None):
        getBox()
        data = []
        print(len(data1))
        for x in range(0,8):
            a = x * 14
            data.append(data0[a],data[a+1],data0[a+2],data0[a+3],data0[a+4],data0[a+5],data0[a+6],data0[a+7],data0[a+8],data0[a+9],data0[a+10],data0[a+11],data0[a+1],data0[a+12],data0[a+13])
            data.append(data1[a],data[a+1],data1[a+2],data1[a+3],data1[a+4],data1[a+5],data1[a+6],data1[a+7],data1[a+8],data1[a+9],data1[a+10],data1[a+11],data1[a+1],data1[a+12],data1[a+13])

        
        filteredplayers = [x for x in players if x not in DNP]
        for x in range(0,len(filteredplayers)):
            a = x * 14
            print(filteredplayers[x] + " |Minutes: " + data[a+1] + " | FGM - FGA: " + data[a+2] + " | FTM - FTA: " + data[a+3] + " | 3PM - 3PA: " + data[a+4] + " | Rebounds: " + data[a+7] + " | Assists: " + data[a+8] + " | Blocks: " + data[a+9] + " | Steals: " + data[a+10] + " | Turnovers: " + data[a+11] + " | Points: " + data[a+13])
            print()
            
nba = NBACLI()
nba.cmdloop()






