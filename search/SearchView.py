from django.conf.urls import url
from django.http.response import HttpResponse
from search.SearchForm import SearchForm
from django.shortcuts import render, redirect
from django.views.generic import View
import requests

from .Keyword import Keywords
from article.Article import Article
from article.credibility import Credibility
# Create your views here.


class SearchView(View):
    def displayArticles(request):
        if 'search' in request.POST:

            form = SearchForm(request.POST)

            searchname = form.getKeyWord()
            print(searchname)
            keywordobjects= Keywords.getArticleList(searchname)

            articles=[]
            emptyList=[]
            for x in keywordobjects:
                print(x.article_id)
                if x.article_id not in emptyList:
                    emptyList.append(x.article_id)
                    articles.append(SearchView.getArticles(x.article_id))     
            print(keywordobjects)
            flag=0
            temp=-1  
            i=0
            while i < len(articles): 
                j=i+1 
                for x in articles[i]: 
                    comp1= x
                while j < len(articles):
                    for y in articles[j]: 
                        comp2= y
                    if comp1.credibility_score < comp2.credibility_score:
                        print("DASDAS")
                        temp = articles[i]
                        articles[i]=articles[j]
                        articles[j]=temp
                    j+=1
                i+=1


            titles = []
            dates = []
            images = []

            for x in range(len(articles)):
                for y in articles[x]:
                    title, date, image = Credibility.getTID(Credibility, y.url)
                    titles.append(title)
                    print(date)
                    dates.append(date)
                    images.append(image)

            xlist = list(zip(articles, titles, dates, images))

            context = {
                'articles': xlist,
            }

            #print(articles[0][0].id)
            
            #print(searchname)
            return render(request, 'result.html', context)

    def getArticles(article_id):
        return Article.getArticle(article_id)