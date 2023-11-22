#created by me 

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""

    if removepunc != "off":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    else:
        return HttpResponse("Error found")

    
    







