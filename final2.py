import json
import re
import sqlite3
import sys
import os
from sqlite3 import Error
# import mysql.connector
import inquirer
import requests

def teamtableabbv(i):#figures out what JSON key to use based on argument
    if i==0:
        abbv='PTS'
    if i==1:
        abbv='REB'
    if i==2:
        abbv='AST'
    if i==3:
        abbv='BLK'
    if i==4:
        abbv='STL'
    if i==5:
        abbv='FG_PCT'
    if i==6:
        abbv='FG3M'
    if i==7:
        abbv='FG3_PCT'
    if i==8:
        abbv='FT_PCT'
    return abbv


def playertableabbv(i):#figures out what JSON key to use based on argument
    if i==0:
        abbv='PTS'
    if i==1:
        abbv='REB'
    if i==2:
        abbv='AST'
    if i==3:
        abbv='BLK'
    if i==4:
        abbv='STL'
    if i==5:
        abbv='TOV'
    if i==6:
        abbv='FG3M'
    if i==7:
        abbv='FTM'
    if i==8:
        abbv='NBA_FANTASY_PTS'
    return abbv

#boiler plate actions, need to get json file and load it
response=requests.get("https://stats.nba.com/js/data/widgets/home_daily.json")
jsonresponse=json.loads(response.text)

####### THIS PORTION OF CODE CREATES LEADER TABLES BASED ON PLAYERS ########
playerstatchoices=jsonresponse['items'][0]['count'] #Number of choices to sort leading players by
try:

    #Creates database in memory--everytime the program is ran new data
    #is collected, keeps leaders current
    conn=sqlite3.connect(':memory:')
except:
    print("Could not connect to database")
i=0;
while i<playerstatchoices:
    # i_players=5 #NBA only gives top 5 players per category
    playercounter=0
    tablename=jsonresponse['items'][0]['items'][i]['title']
    var=playertableabbv(i)
    cur=conn.cursor()
    pattern=" "
    tablename2=re.sub(pattern, "_",tablename)
    createexecutestring='''CREATE TABLE IF NOT EXISTS {}(player_name text NOT NULL, player_abbv text NOT NULL, player_score text NOT NULL)'''.format("player"+tablename2)
    try:
        cur.execute(createexecutestring)
    except:
        print("Table could not be created")

    # while playercounter<i_players:
    for item in jsonresponse['items'][0]['items'][i]['playerstats']:
        player_name=jsonresponse['items'][0]['items'][i]['playerstats'][playercounter]['PLAYER_NAME']
        player_abbv=jsonresponse['items'][0]['items'][i]['playerstats'][playercounter]['TEAM_ABBREVIATION']
        player_score=jsonresponse['items'][0]['items'][i]['playerstats'][playercounter][var]
        try:
            insert='INSERT INTO {} VALUES (?,?,?)'.format("player"+tablename2)
            cur.execute(insert,(player_name, player_abbv, player_score))
            conn.commit()
        except:
            print("CANNOT INSERT DATA INTO TABLE.")
        playercounter+=1
    i+=1


#######THIS PORTION OF CODE CREATES LEADER TABLES BASED ON TEAMS###########
teams=jsonresponse['items'][1]['uid']
teamstatchoices=jsonresponse['items'][1]['count'] #Number of leader options
j=0

while j<teamstatchoices:
    # i_teams=2
    teamcounter=0
    teamtablename=jsonresponse['items'][1]['items'][j]['title']
    # print(teamtablename)
    var=teamtableabbv(j)
    cur=conn.cursor()
    pattern=" "
    teamtablename2=re.sub(pattern, "_",teamtablename)
    createexecutestring='''CREATE TABLE IF NOT EXISTS {}(team_name text NOT NULL, team_abbv text NOT NULL, team_score text NOT NULL)'''.format("team"+teamtablename2)
    try:
        cur.execute(createexecutestring)
    except:
        print("Table could not be created")

    for item in jsonresponse['items'][1]['items'][j]['teamstats']:
        #NBA changes number of leading teams based on how many teams are currently
        #playing when the program is ran. If no teams, NBA will default to 5
        team_name=jsonresponse['items'][1]['items'][j]['teamstats'][teamcounter]['TEAM_NAME']
        team_abbv=jsonresponse['items'][1]['items'][j]['teamstats'][teamcounter]['TEAM_ABBREVIATION']
        team_score=jsonresponse['items'][1]['items'][j]['teamstats'][teamcounter][var]
        try:
            insert='INSERT INTO {} VALUES (?,?,?)'.format("team"+teamtablename2)
            cur.execute(insert,(team_name,team_abbv, team_score))
            conn.commit()
            # print(team_name + " was added to database")
        except:
            print("CANNOT INSERT DATA INTO TABLE.")
        teamcounter+=1
    j+=1
###THIS PORTION OF CODE PROMPTS THE USER FOR THEIR SELECTIONS########
askagain=True;
while askagain==True:
    initialquestion=[
        inquirer.List('playerorteam', message="Would you like leaders based on players or teams?", choices=['Players','Teams'], carousel=True),
    ]
    answer=inquirer.prompt(initialquestion)
    if answer["playerorteam"]=="Players":
        chooseplayerstat=[
        inquirer.List('whatstat', message="What category would you like to see?", choices=['Points','Rebounds', 'Assists','Blocks','Steals','Turnovers','Three Pointers Made', 'Free Throws Made', 'Fantasy Points'], carousel=True)
        ]
        choice=inquirer.prompt(chooseplayerstat)
        if choice["whatstat"]=="Points":
            for row in cur.execute("SELECT * FROM playerPoints ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Rebounds":
            for row in cur.execute("SELECT * FROM playerRebounds ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Assists":
            for row in cur.execute("SELECT * FROM playerAssists ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Blocks":
            for row in cur.execute("SELECT * FROM playerBlocks ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Steals":
            for row in cur.execute("SELECT * FROM playerSteals ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Turnovers":
            for row in cur.execute("SELECT * FROM playerTurnovers ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Three Pointers Made":
            for row in cur.execute("SELECT * FROM playerThree_Pointers_Made ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Free Throws Made":
            for row in cur.execute("SELECT * FROM playerFree_Throws_Made ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Fantasy Points":
            for row in cur.execute("SELECT * FROM playerFantasy_Points ORDER BY ROWID"):
                print(row)


    if answer["playerorteam"]=="Teams":
        chooseplayerstat=[
        inquirer.List('whatstat', message="What category would you like to see?", choices=['Points','Rebounds', 'Assists','Blocks','Steals','Field Goal Percentage','Three Pointers Made', 'Three Point Percentage', 'Free Throw Percentage'], carousel=True)
        ]
        choice=inquirer.prompt(chooseplayerstat)
        if choice["whatstat"]=="Points":
            for row in cur.execute("SELECT * FROM teamPoints ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Rebounds":
            for row in cur.execute("SELECT * FROM teamRebounds ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Assists":
            for row in cur.execute("SELECT * FROM teamAssists ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Blocks":
            for row in cur.execute("SELECT * FROM teamBlocks ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Steals":
            for row in cur.execute("SELECT * FROM teamSteals ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Field Goal Percentage":
            for row in cur.execute("SELECT * FROM teamField_Goal_Percentage ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Three Pointers Made":
            for row in cur.execute("SELECT * FROM teamThree_Pointers_made ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Three Point Percentage":
            for row in cur.execute("SELECT * FROM teamThree_Point_Percentage ORDER BY ROWID"):
                print(row)
        if choice["whatstat"]=="Free Throw Percentage":
            for row in cur.execute("SELECT * FROM teamFree_Throw_Percentage ORDER BY ROWID"):
                print(row)
    shouldcontinue=[
        inquirer.Confirm('keepgoing', message="Would you like to make another selection?"),]
    yesno=inquirer.prompt(shouldcontinue)
    if yesno['keepgoing']==True:
        askagain=True
    if yesno['keepgoing']==False:
        askagain=False
