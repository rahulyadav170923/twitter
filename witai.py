from wit import Wit
client = Wit(access_token='O4UTIIG6GRCS2EWZBWDUDZF4E5P7SYY2')

def getchannel(tweet):
    resp = client.message(tweet)
    if resp['entities']['entity'][0]['value'] :
        return resp['entities']['entity'][0]['value']