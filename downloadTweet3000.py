import tweepy
import re
auth = tweepy.OAuthHandler("c7qXOTlbr7EdDorhu8b3kh2un","LleVP4h3B9LiyobNkFY5H3YY64MuCZWBxOXxN9sYUGLGc5JPRR")
auth.set_access_token("857028354-IewjwNOVNMzROqrINYaubFr45eUN9cnDaiLZdsgC","cWgsqFWjjP5YzMyBSpjb80tLAdppF04yJPez1CxzpuMZi")

api = tweepy.API(auth)
def saida_txt(tweet):
    with open('down3000.txt', 'a') as f:
            f.write(tweet + '\n')

public_tweets = api.user_timeline("@USATODAY",count=800)
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@WSJ",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@washingtonpost",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@FoxNews",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@CBSNews",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@CNN",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@nytimes",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@TIME",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@NBCNews",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@SkyNews",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@BBCBreaking",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@ABC",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))

public_tweets = api.user_timeline("@latimes",count=800) #CNN, usatoday, time, huffpost, LATIMES, WALL STREET JOURNALS, washingtonpost, NBCNEWS, SKYNEWS,BBCBREAKING, NYTIMES, CBS, ABC, FoxNews
for tweet in public_tweets:
    #print(tweet.text.encode("utf-8"))
    saida_txt(tweet.text.encode("utf-8"))
