import requests, json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import winsound
import tkinter
from tkinter import messagebox
from bs4 import BeautifulSoup

#Important Source Documents:
#Unofficial update lolesports API :https://gist.github.com/brcooley/8429583561c47b248f80
#Gspread API : https://github.com/burnash/gspread
def scrapeDataNA():
    #Scrapes data from Gamepedias webpage.
    games = []
    headers = {
    'User-Agent': 'NukeWolfs, NuclearWolf#3425',
    'From': 'nebraskatest@gmail.com'
    }
    ck = {'id_token':'eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjY2VjMjlhNS04ODM2LTU4ZjUtYTY3My01M2QyZGFkMjMyNWUiLCJjb3VudHJ5IjoidXNhIiwiYW1yIjpbInBhc3N3b3JkIl0sImlzcyI6Imh0dHBzOlwvXC9hdXRoLnJpb3RnYW1lcy5jb20iLCJsb2wiOlt7ImN1aWQiOjIyNzYxMzc4MCwiY3BpZCI6Ik5BMSIsInVpZCI6MjI3NjEzNzgwLCJ1bmFtZSI6Ik51a2VzV29sZnMiLCJwdHJpZCI6bnVsbCwicGlkIjoiTkExIiwic3RhdGUiOiJFTkFCTEVEIn1dLCJsb2NhbGUiOiJlbl9VUyIsImF1ZCI6InJzby13ZWItY2xpZW50LXByb2QiLCJhY3IiOiJ1cm46cmlvdDpicm9uemUiLCJleHAiOjE1Nzc0MjM1NTgsImlhdCI6MTU3NzMzNzE1OCwiYWNjdCI6eyJnYW1lX25hbWUiOiJOdWtlV29sZnMiLCJ0YWdfbGluZSI6Ik5BIn0sImp0aSI6InJ2MjNSUVZtdENJIiwibG9naW5fY291bnRyeSI6InVzYSJ9.bRM70_TOsCKszk88XQCSeIXTg3qnBltpRBuE_MBpTr_RtD4gM3iwYoJllKDOtnDxnaZdnKHVTYk1ehwJVsjKqCC3GBbkPjkj7DSVVRf4cSGsCiwKq3RF9XoeXTKehwsuCoQXDPYPxwi0MbF56YxKFU1-oMMpClbMrc7-wy7VNg0'}
    page = requests.get('https://lol.gamepedia.com/LCS/2020_Season/Spring_Season', headers = headers, cookies=ck)
    soup = BeautifulSoup(page.text, 'html.parser')
    Match_History = soup.find(class_='wikitable md-table')
    MHLinks = Match_History.find_all('tr', attrs={"class": "mdv-allweeks mdv-week"+str(weak)})
    print(len(MHLinks))
    for link in MHLinks:
        minSub = str(link).find('leagueoflegends.com/en/#match-details/')
        maxSub = str(link).find('"',minSub)
        if(minSub != -1):
            link = str(link)[int(minSub)+38:maxSub]
            games.append(link)
    print(len(games))
    return games
def scrapeDataEU():
    #Scrapes data from the other webpage.
    games = []
    headers = {
    'User-Agent': 'NukeWolfs, NuclearWolf#3425',
    'From': 'nebraskatest@gmail.com'
    }
    ck = {'id_token':'eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjY2VjMjlhNS04ODM2LTU4ZjUtYTY3My01M2QyZGFkMjMyNWUiLCJjb3VudHJ5IjoidXNhIiwiYW1yIjpbInBhc3N3b3JkIl0sImlzcyI6Imh0dHBzOlwvXC9hdXRoLnJpb3RnYW1lcy5jb20iLCJsb2wiOlt7ImN1aWQiOjIyNzYxMzc4MCwiY3BpZCI6Ik5BMSIsInVpZCI6MjI3NjEzNzgwLCJ1bmFtZSI6Ik51a2VzV29sZnMiLCJwdHJpZCI6bnVsbCwicGlkIjoiTkExIiwic3RhdGUiOiJFTkFCTEVEIn1dLCJsb2NhbGUiOiJlbl9VUyIsImF1ZCI6InJzby13ZWItY2xpZW50LXByb2QiLCJhY3IiOiJ1cm46cmlvdDpicm9uemUiLCJleHAiOjE1Nzc0MjM1NTgsImlhdCI6MTU3NzMzNzE1OCwiYWNjdCI6eyJnYW1lX25hbWUiOiJOdWtlV29sZnMiLCJ0YWdfbGluZSI6Ik5BIn0sImp0aSI6InJ2MjNSUVZtdENJIiwibG9naW5fY291bnRyeSI6InVzYSJ9.bRM70_TOsCKszk88XQCSeIXTg3qnBltpRBuE_MBpTr_RtD4gM3iwYoJllKDOtnDxnaZdnKHVTYk1ehwJVsjKqCC3GBbkPjkj7DSVVRf4cSGsCiwKq3RF9XoeXTKehwsuCoQXDPYPxwi0MbF56YxKFU1-oMMpClbMrc7-wy7VNg0'}

    page = requests.get('https://lol.gamepedia.com/LEC/2020_Season/Spring_Season', headers = headers,cookies=ck)
    soup = BeautifulSoup(page.text, 'html.parser')
    Match_History = soup.find(class_='wikitable md-table')
    print(Match_History)
    MHLinks = Match_History.find_all('tr', attrs={"class": "mdv-allweeks mdv-week"+str(weak)})
    print(len(MHLinks))
    for link in MHLinks:
        minSub = str(link).find('/#match-details/')
        print(link)
        maxSub = str(link).find('"',minSub)
        if(minSub != -1):
            link = str(link)[int(minSub)+16:maxSub]
            games.append(link)
    print(len(games))
    #Returns a link to the match history site
    return games

def verifyWeek(week,games):
    verifiedGames=[]
    region = "cool"
    #Takes in all games of the split and grabs match data on week and hash data
    for index  in range(len(games)):
        global tournamentID
        URL = 'http://api.lolesports.com/api/v2/highlanderMatchDetails?tournamentId='+tournamentID+'&matchId='+games[index]['matchID']
        
        r  = requests.get(URL)
        matchData = json.loads(r.text)
    
        #Takes the match data and checks if it is the correct week and than creates a new list of matchhistory data to access
        if (matchData['scheduleItems'][0]['tags']['blockLabel'] == week):
          #  if 'gameHash' in matchData['gameIdMappings'][0]:
            try:
                check = games[index]['realm']+'/'+games[index]['matchHistoryId']+'?gameHash='+matchData['gameIdMappings'][0]['gameHash']
                if (not (check == 'ESPORTSTMNT01/1074560?gameHash=6a89b0a79afa77c8')):
                    verifiedGames.append(games[index]['realm']+'/'+games[index]['matchHistoryId']+'?gameHash='+matchData['gameIdMappings'][0]['gameHash'])
                    region = matchData['players'][0]['region']
                    print ('Currently verifying games from the ' + region + ' . . .')
            except IndexError:
                time.sleep(.05)
    
    #Checks if there are 10 games for each week
    print("There are "+str(len(verifiedGames))+" verified matches in week "+str(week)+" of the " +region)
    return verifiedGames

def getSheet():
    #Basic Authorization of the google spread sheet requested and reuturns a sheet
    
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds= ServiceAccountCredentials.from_json_keyfile_name('my-project-1546570563654-707aa270350b.json', scope)
    client = gspread.authorize(creds)
    
    return client.open('FantasyLCSPlayerPoints Spring 2020').worksheet("Week"+str(int(weak)))
    #return client.open('FantasyLCSPlayerPoints').worksheet("TestSheet")      
        
def addScore(player,number,sheet):
    #Add player scores to spreadsheets by finding cell and replacing it, if it does not find a certain player, it will add a new cell.
    time.sleep(2)
    try:
        cell= sheet.find(player)
        sheet.update_cell(cell.row,2,number + float(sheet.cell(cell.row,2).value))
        row = cell.row
    except gspread.exceptions.CellNotFound:
        values_list = sheet.col_values(1)
        cell = sheet.find(values_list[-1])
        sheet.update_cell(cell.row+1,1,player)
        sheet.update_cell(cell.row+1,2,0)
        sheet.update_cell(cell.row+1,2,number+ float(sheet.cell(cell.row+1,2).value))
        time.sleep(1)
        sheet.update_cell(cell.row+1,3,0)
        row = cell.row+1
    return row
def addGame(gameData,score,row,sheet,link):
    time.sleep(2)
    t1 = gameData['participantIdentities'][0]['player']['summonerName']
    t1 = t1[:t1.find(" ")]
    t2 = gameData['participantIdentities'][7]['player']['summonerName']
    t2 = t2[:t2.find(" ")]
    score = str(score)
    if len(score)>5:
        score = score[:5]
    if (sheet.cell(row,4).value == ""):
        sheet.update_cell(row,4,'=HYPERLINK("'+link+'","'+str(score)+"("+t1+"-vs-"+t2+")"+'")')
    else:
        sheet.update_cell(row,5,'=HYPERLINK("'+link+'","'+str(score)+"("+t1+"-vs-"+t2+")"+'")')
    time.sleep(2)
    sheet.update_cell(row,3,1+ float(sheet.cell(row,3).value))

        
def addTimerScore(number,sheet):
    sheet.update_cell(3,4,number + float(sheet.cell(3,4).value))
def clearScore(sheet):
    values_list = sheet.col_values(1)
    cell = sheet.find(values_list[-1])
    for index in range(cell.row):
        time.sleep(2)
        sheet.update_cell(index+2,2,0)
        time.sleep(2)
        sheet.update_cell(index+2,3,0)
        time.sleep(2)
        sheet.update_cell(index+2,4,"")
        time.sleep(2)
        sheet.update_cell(index+2,5,"")
def getPlayerData(games):
    sheet = getSheet()
    for index in range(len(games)):
        print(str(index*10+10) + "%")
        URL = "https://acs.leagueoflegends.com/v1/stats/game/"+games[index]
        ck = {'id_token':'eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjY2VjMjlhNS04ODM2LTU4ZjUtYTY3My01M2QyZGFkMjMyNWUiLCJjb3VudHJ5IjoidXNhIiwiYW1yIjpbInBhc3N3b3JkIl0sImlzcyI6Imh0dHBzOlwvXC9hdXRoLnJpb3RnYW1lcy5jb20iLCJsb2wiOlt7ImN1aWQiOjIyNzYxMzc4MCwiY3BpZCI6Ik5BMSIsInVpZCI6MjI3NjEzNzgwLCJ1bmFtZSI6Ik51a2VzV29sZnMiLCJwdHJpZCI6bnVsbCwicGlkIjoiTkExIiwic3RhdGUiOiJFTkFCTEVEIn1dLCJsb2NhbGUiOiJlbl9VUyIsImF1ZCI6InJzby13ZWItY2xpZW50LXByb2QiLCJhY3IiOiJ1cm46cmlvdDpicm9uemUiLCJleHAiOjE1Nzc0MjM1NTgsImlhdCI6MTU3NzMzNzE1OCwiYWNjdCI6eyJnYW1lX25hbWUiOiJOdWtlV29sZnMiLCJ0YWdfbGluZSI6Ik5BIn0sImp0aSI6InJ2MjNSUVZtdENJIiwibG9naW5fY291bnRyeSI6InVzYSJ9.bRM70_TOsCKszk88XQCSeIXTg3qnBltpRBuE_MBpTr_RtD4gM3iwYoJllKDOtnDxnaZdnKHVTYk1ehwJVsjKqCC3GBbkPjkj7DSVVRf4cSGsCiwKq3RF9XoeXTKehwsuCoQXDPYPxwi0MbF56YxKFU1-oMMpClbMrc7-wy7VNg0'}

        print(URL)
        print(games[index])
        r  = requests.get(URL,cookies=ck)
        gameData = json.loads(r.text)
        #gets score for each player and assigns it into google doc spread sheet
        for index1 in range(10):
            score = getPlayerScore(gameData['participants'][index1]['stats'],'https://matchhistory.na.leagueoflegends.com/en/#match-details/'+games[index])
            identity = gameData['participantIdentities'][index1]['player']['summonerName']
            identity = identity[identity.find(" ")+1:]
            row = addScore(identity,score,sheet)
            addGame(gameData,score,row,sheet,'https://matchhistory.na.leagueoflegends.com/en/#match-details/'+games[index])
            
        for index1 in range(2):
            score = getTeamScore(gameData['teams'][index1],gameData['gameDuration'])
            identity = gameData['participantIdentities'][index1*6]['player']['summonerName']
            identity = identity[:identity.find(" ")]
            row = addScore(identity,score,sheet)
            addGame(gameData,score,row,sheet,'https://matchhistory.na.leagueoflegends.com/en/#match-details/'+games[index])
            
            
def getPlayerScore(person,link):
    #gets a score
    score = 0
    kills = person['kills']
    deaths = person['deaths']
    assists = person['assists']
    creeps = person['totalMinionsKilled'] + person['neutralMinionsKilled']
    tripleKills = person['tripleKills']
    quadraKills = person ['quadraKills']
    pentaKills = person ['pentaKills']
    if quadraKills>=1 or pentaKills>=1:
        file = open("multikill.txt", "r")
        b = True
        for line in file:
            print( line)
            x = line.split()
            if x[0]==(""+str(kills)+str(deaths)+str(assists)+str(creeps)):
                tripleKills = x[1]
                quadraKills = x[2]
                pentaKills = x[3]
                b = False
        if(b):
            file.close()
            winsound.Beep(100,5000)
            print("Please Manually Check for Triple, Quadra, and Pentakills in the timeline for the person with "+str(kills)+" kills and "+str(creeps)+" cs at: \n"+link)
            tripleKills = input('Please Type in # of TripleKills')
            quadraKills = input('Please type in # of QuadraKills')
            pentaKills = input('Please type in # of PentaKills')
            file = open('multikill.txt', 'a')
            file.write("\n"+str(kills)+str(deaths)+str(assists)+str(creeps)+" "+str(tripleKills)+" "+str(quadraKills)+" "+str(pentaKills))
            file.close()
    
        
    score = (kills*2) + (deaths *-1) + (1.5*assists) + (creeps*.01) + (int(tripleKills)*2) + (int(quadraKills)*5)+ + (int(pentaKills)*10)
    
            
    if assists >=10 or kills>=10:
        score +=2
    return score

def getTeamScore(team,gamelength):
    score = 0
    win = 0
    firstBlood = 0
    if team['win'] == 'Win':
        if gamelength<1800:
            win = 4
        else:
            win = 2
    if team['firstBlood']:
        firstBlood=2
    baron = team['baronKills']
    dragon = team['dragonKills']
    towers = team['towerKills']
    rift = team["riftHeraldKills"]
    score = win + firstBlood + baron*2 + dragon + towers + rift
    return score
def liveUpdate():
    checked=[]
    global NAlive
    global EUlive
    while True:
        #Processes all the data for EU
        if EUlive:
            pseudoGames = []
            #Gets a list of al the games played in the week of the games
            verifiedGames=scrapeDataEU()
            #Checks if the game has been already checked or not this session
            for index in range(len(verifiedGames)):
                if verifiedGames[index] in checked:
                    verifiedGames[index] = 'nope'
                else:
                    checked.append(verifiedGames[index])
            #PseudoGames represents new games that need to be checked.
            for index in verifiedGames:
                if index != 'nope':
                    pseudoGames.append(index)
            print(checked)
            print(pseudoGames)
            if len(pseudoGames) >0:
                #Sends links of the games to be processed.
                  getPlayerData(pseudoGames)
        if NAlive:
            pseudoGames = []
            verifiedGames=scrapeDataNA()
            for index in range(len(verifiedGames)):
                if verifiedGames[index] in checked:
                    verifiedGames[index] = 'nope'
                else:
                    checked.append(verifiedGames[index])
            for index in verifiedGames:
                if index != 'nope':
                    pseudoGames.append(index)
            print(checked)
            for x in pseudoGames:
                print("https://matchhistory.na.leagueoflegends.com/en/#match-details/"+x)
            if len(pseudoGames) >0:
                  getPlayerData(pseudoGames)
        time.sleep(60)
        
if __name__ == '__main__':
    print("Welcome to the League Fantasy Calculator\nMake sure your spreadsheet is shared to edit with")
    print("*Notice, Last week of LCS may not be accurate")
    
    week = input("Enter the Week you would like to calculate")
    root= tkinter.Tk()
    global NAlive
    global EUlive
    NAlive = messagebox.askyesno("Title","Calculate NA?")
    EUlive = messagebox.askyesno("Title","Calculate EU?")
    root.destroy()
    
    global weak
    weak = week
    #clearScore(getSheet())

#    verifiedGames = ["ESPORTSTMNT01/1165751?gameHash=d52dc94a0069bf6c",
#                     ]
#   getPlayerData(verifiedGames)
    liveUpdate()

    