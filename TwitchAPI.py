import requests

def channelSub(channel):
    URL = 'https://api.twitch.tv/kraken/channels/'+channel+'/subscriptions'
    response = requests.get(URL)
    return response


print('Which channel would you like to look up?')
channel = input()

channelSubs = channelSub(channel)
print(channelSubs)
