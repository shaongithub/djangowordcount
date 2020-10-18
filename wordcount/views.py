from django.http import HttpResponse
from django.shortcuts import render
from . import views

def home(request):
    '''
    home page
    '''
    return render(request, 'home.html')

def about(request):
    '''
    about page
    '''
    return render(request, 'about.html')

def count(request):
    '''
    count page
    '''
    fulltext = request.GET['fulltext']

    letterCount = 0
    for i in fulltext:
        if i != ' ':
            letterCount += 1
    
    wordlist = fulltext.split()

    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist), 'letterCount': letterCount})
