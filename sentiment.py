import indicoio
indicoio.config.api_key = 'f11b01c5fa06a94f61dbbef5d9175840'

def getsentiment(tweet):
    i=indicoio.sentiment_hq(tweet)
    if i<0.5 :
        return 'negative'
    return 'positive'
