from django.shortcuts import render,redirect
from django.http import HttpResponse
from newsapi import NewsApiClient
from datetime import date, timedelta
import json
consumer_key= 'NUkOrdTkVSd5AKqKetajGWVaO' #API_KEY(Twitter)
consumer_secret= 'ZooIHc9DrgVTuTU96XDYGvZF54wavk3aNKWd3fyZLzIGxGgbF6' 
access_token= '877839641344430080-knj2CUZn4LbZ1O57mgJEbRQ1fVdUODP' 
access_token_secret= 'mv34QLXYsUab0qgvXOHQWV5dp7vfPuXwFDhcYkFrDl5JJ' 
APIKEY="141f860e070f4dc4a86c383f9d5604fc" 
import urllib.parse
import tweepy as tw

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

newsapi = NewsApiClient(api_key=APIKEY) #newsAPI
current_date = date.today().isoformat()   
days_before = (date.today()-timedelta(days=25)).isoformat()

def clean_input(tag):
    tag = tag.replace(" ", "")
    if tag.startswith('#'):
        return tag[1:].lower()
    else:
        return tag.lower()

def return_all_hashtags(tweets, tag):
    all_hashtags = []
    for tweet in tweets:
        for word in tweet.split():
            if word.startswith('#') and word.lower() != '#' + tag.lower():
                all_hashtags.append(word.lower())
    return all_hashtags

def get_hashtags(tag):
    search_tag = clean_input(tag)
    tweets = tw.Cursor(api.search,q='#' + search_tag,lang="en").items(50)
    tweets_list = []
    for tweet in tweets:
        tweets_list.append(tweet.text)
    all_tags = return_all_hashtags(tweets_list, tag)
    frequency = {}
    for item in set(all_tags):
        frequency[item] = all_tags.count(item)
    return {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1], reverse=True)}

#######.............................................................
# print(current_date, days_before)
# all_indian_sources=newsapi.get_sources(language='en',country='in')
# all_indian_sources=all_indian_sources['sources']
# print(all_indian_sources)

def index(request):
    page_no = int(request.GET.get('page_no', 1))
    topheadlines=newsapi.get_top_headlines(sources='google-news-in,the-hindu,the-times-of-india,espn',language='en',page_size=5, page=int(page_no))
    articles=topheadlines['articles']
    # print(articles)
    desc = []
    news = []
    img = []
    auth = []
    pubat = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]
        url.append(myarticles['url'])
        auth.append(myarticles['author'])
        time = myarticles['publishedAt']
        # temp = str(time.date()) + " @ " + str(time.time())
        temp= time[8:10]+'-'+time[5:7]+'-'+time[:4] + " @ " + time[11:19]
        # print(type(time),time,temp)
        pubat.append(temp)
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img, auth, pubat, url)

    return render(request, 'index.html', {"mylist": mylist, "page_no": page_no})

def search(request):
    if request.method == 'GET':
        query=request.GET.get('search_for',None)

        if query is None:
            return redirect('')
        else:
            page_no = int(request.GET.get('page_no', 1))
            # print(encoded)
            # particular_topic = newsapi.get_top_headlines(qintitle='{}'.format(query),country='in',page=1)
            tag =str(query)
            particular_topic = newsapi.get_everything(qintitle=query,from_param=days_before,to=current_date,sources='google-news-in,the-hindu,the-times-of-india,espn',language='en',sort_by='publishedAt',page_size=5, page=page_no)
            articles=particular_topic['articles']
            # print(query, articles)
            desc = [] 
            news = [] 
            img = [] 
            auth = [] 
            pubat = [] 
            url = [] 
            for i in range(len(articles)):
                myarticles = articles[i]
                url.append(myarticles['url'])
                auth.append(myarticles['author'])
                time = myarticles['publishedAt']
                # temp = str(time.date()) + " @ " + str(time.time())
                temp= time[8:10]+'-'+time[5:7]+'-'+time[:4] + " @ " + time[11:19]
                # print(type(time),time,temp)
                pubat.append(temp)
                news.append(myarticles['title'])
                desc.append(myarticles['description'])
                img.append(myarticles['urlToImage'])

            mylist = zip(news, desc, img, auth, pubat, url)
            all_tags = get_hashtags(tag)
            return render(request, 'search.html', {'mylist':mylist , 'query':query, 'data':all_tags, 'page_no': page_no},)