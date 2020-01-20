from django.http import HttpResponse
from django.shortcuts import render
from . import views

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist)})
