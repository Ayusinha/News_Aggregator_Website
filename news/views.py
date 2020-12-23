from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient

def index(request):
    newsapi = NewsApiClient(api_key="141f860e070f4dc4a86c383f9d5604fc")
    topheadlines=newsapi.get_top_headlines(sources='bbc-news,the-verge,google-news-in,google-news,hacker-news,national-geographic,news24,reuters,techcrunch-cn,the-hindu,the-times-of-india',language='en',page=5)
    
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
        pubat.append(myarticles['publishedAt'])
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img, auth, pubat, url)

    return render(request, 'index.html', context={"mylist":mylist})