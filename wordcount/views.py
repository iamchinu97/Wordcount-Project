from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def countwords(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    print(fulltext)

    worddiction={}

    for word in wordlist:
        if word in worddiction:
            worddiction[word]+=1
        else:
            worddiction[word]=1

    return render(request,'count.html',{'fulltext':fulltext,'length':len(wordlist),'sortedlist':worddiction.items()})
