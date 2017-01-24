# Riot API key: c6f81fdd-d131-4ae2-b100-934362df5e1e

import requests

def getSummonerID(region, summoner):
    URL = 'https://'+region+'.api.pvp.net/api/lol/'+region+'/v1.4/summoner/by-name/'+summoner+\
          '?api_key=c6f81fdd-d131-4ae2-b100-934362df5e1e'

    response = requests.get(URL)
    return response.json()


def championByID(champID):
    URL = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/'+str(champID)+\
          '?api_key=c6f81fdd-d131-4ae2-b100-934362df5e1e'
    response = requests.get(URL)
    return response.json()


# Season 2015
def summonerStatsSummary(region, summonerID):
    URL = 'https://'+region+'.api.pvp.net/api/lol/'+region+'/v1.3/stats/by-summoner/'+str(summonerID)+\
          '/summary?season=SEASON2015&api_key=c6f81fdd-d131-4ae2-b100-934362df5e1e'
    response = requests.get(URL)
    return response.json()

# Search for unranked hours
def unrankedHours(summonerStats):
    i=0
    while(True):
        if(summonerStats['playerStatSummaries'][i]['playerStatSummaryType']=='Unranked'):
            wins = summonerStats['playerStatSummaries'][i]['wins']
            a = wins*2
            a = 2*wins*35
            print(str(a)+' mins with a total of ' + str(wins) + ' wins and ~ '+ str((wins*2)) + 'games',end='\n')
            a= float(a/60)
            print('which is a total of '+str(a)+' hours')
            break
        else:
            i+=1

    return summonerStats


def rankedStatsByChamp(region, summonerID):
    URL = 'https://'+region+'.api.pvp.net/api/lol/'+region+'/v2.5/league/by-summoner/'+str(summonerID)+\
          '?api_key=c6f81fdd-d131-4ae2-b100-934362df5e1e'
    response = requests.get(URL)
    return response.json()


def recentMatches(region, summonerID):
    URL = 'https://'+region+'.api.pvp.net/api/lol/'+region+'/v1.3/game/by-summoner/'+summonerID+\
          '/recent?api_key=c6f81fdd-d131-4ae2-b100-934362df5e1e'
    response = requests.get(URL)
    return response.json()


# Main method start------------------------------------------------------------------------------------------------
print('Enter your region \n')
print('enter from: br, eune, euw, kr, lan, na')
region = input()


# loop if the entered region is not in the list
while(region!='br' or region!='euw' or region!='kr' or region!='lan' or region!='na'):
    if(region=='br' or region=='euw' or region=='kr' or region=='lan' or region=='na'):
        break
    print('\nEnter your region \n')
    print('enter from: br, eune, euw, kr, lan, na')
    region = input()
    if(region=='br' or region=='euw' or region=='kr' or region=='lan' or region=='na'):
        break
    
print('Enter your summoner name: ')
summoner = input()

summoner = str(summoner)
summoner = summoner.lower()
summoner = summoner.replace(" ", "")

print(region, summoner, sep=' ')

response1 = getSummonerID(region, summoner)
id = response1[summoner]['id']
print(response1,end='\n')
print(id)
id = str(id)

# loop so we dont have to enter region and stuff everytime and restart program---------------

while(True):
    print('what would you like to do? \n \n "exitf, champID, unrankedStats, hours, avgCS, rankedStats, changeSummoner,'
          ' cs@10"')
    response = input()

    print("Print response: "+response)



    if response not in ["exitf", "champID", "unrankedStats", "hours","avgCS", "rankedStats", "changeSummoner", "cs@10"]:
        continue


    elif(response == "changeSummoner"):

        print('Enter your region \n')
        print('enter from: br, eune, euw, kr, lan, na')
        region = input()


        # loop if the entered region is not in the list
        while(region!='br' or region!='euw' or region!='kr' or region!='lan' or region!='na'):
            if(region=='br' or region=='euw' or region=='kr' or region=='lan' or region=='na'):
                break
            print('\nEnter your region \n')
            print('enter from: br, eune, euw, kr, lan, na')
            region = input()
            if(region=='br' or region=='euw' or region=='kr' or region=='lan' or region=='na'):
                break

        print('Enter your summoner name: ')
        summoner = input()
        summoner = str(summoner)
        # lowercase the input
        summoner = summoner.lower()
        summoner = summoner.replace(" ", "")

        print(region, summoner, sep=' ')

        response1 = getSummonerID(region, summoner)
        id = response1[summoner]['id']
        print(response1,end='\n')
        print(id)
        id = str(id)
        continue


    elif(response=="exitf"):
        break


    elif(response=="champID"):       
    #Champion by ID prints name and the champions title
        print('\n enter champion ID to get name as well the title (i.e. 42): ', end='')
        champID = input()
        response3 = championByID(champID)
        print(response3)
        print(response3['name'] + '\n' + response3['title'])


    elif(response=='unrankedStats'):

    # Get Ranked Stats
        summonerStats = summonerStatsSummary(region, id)

        a = len(summonerStats['playerStatSummaries'])
    # prints stats from unranked games for Season 2015

        print('total Minions Killed = '+str(summonerStats['playerStatSummaries'][a-1]['aggregatedStats']
                                            ['totalMinionKills']), end='\n')
        print('total champion kills = '+str(summonerStats['playerStatSummaries'][a-1]['aggregatedStats']
                                            ['totalChampionKills']), end='\n')
        print('total turrets killed = '+str(summonerStats['playerStatSummaries'][a-1]['aggregatedStats']
                                            ['totalTurretsKilled']), end='\n')
        print('total neutral Minions = '+str(summonerStats['playerStatSummaries'][a-1]['aggregatedStats']
                                             ['totalNeutralMinionsKilled']), end='\n')
        print('total assists = '+str(summonerStats['playerStatSummaries'][a-1]['aggregatedStats']['totalAssists']),
              end='\n')
        print('total Unranked wins = '+str(summonerStats['playerStatSummaries'][a-1]['wins']), end='\n')


    elif(response=='hours'):
        summonerStats = summonerStatsSummary(region, id)
        print('\n')
        print('Assuming you have a 50% win rate, and also assuming your games lasted ~35 mins, your total time wasted'
              ' on LoL is:')
        print('\n')
        unrankedHours(summonerStats)


    elif(response=='avgCS'):
        summonerStats = summonerStatsSummary(region, id)

       # Find length of array to compensate for when people have less items in list
        a = len(summonerStats['playerStatSummaries'])


        totMinKilled = summonerStats['playerStatSummaries'][a-1]['aggregatedStats']['totalMinionKills']
        neutralMin = summonerStats['playerStatSummaries'][a-1]['aggregatedStats']['totalNeutralMinionsKilled']
        totMinKilled += neutralMin
        wins = summonerStats['playerStatSummaries'][a-1]['wins']
        totGames = wins*2
        avgCS = float(totMinKilled/totGames)
        print('your average CS for '+str(totGames)+' games is '+str(avgCS)+' per game')


    elif(response=='rankedStats'):
        rankedStats = rankedStatsByChamp(region,id)
        print(rankedStats)
        print('\n')
        print('   Tier: '+rankedStats[id][0]['tier'])
        print('\n')


# Lists recent games. Asks users for which game to get cs@10 from. Prints the cs @ 10
    elif(response=='cs@10'):
        matches = recentMatches(region, id)

        print('Which game would you like the cs@10 from?\n')
        print('Pick the number next to the champion to get the details.')
        print('\n')
        for i in range (0, len(matches['games'])):
            # print((matches['games'][i]['championId']), end=', ')

            champResponse = championByID(matches['games'][i]['championId'])
            if(i==len(matches['games'])-1):
                print(str(i)+' '+champResponse['name'], end='')
            else:
                print(str(i)+' '+champResponse['name'], end=', ')

        print('\n')
        print('Which champion from the recent game would you like to look up the cs@10 for? (Enter only int#)')
        num = input()

        champResponse = championByID(matches['games'][int(num)]['championId'])
        print('cs@10 for '+champResponse['name']+' is: ')

        print('\n')

