from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    # return HttpResponse('<h1>你真可爱</h1>')
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')


# def eggs(request):
#     return HttpResponse('<h1>付晓，您配钥匙🔑吗，您配个几把啊？</h1>')
def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)


    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
