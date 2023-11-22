
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):

    djtext = request.POST.get('text', 'default')
    fullcaps = request.POST.get('fullcaps', 'off')
    Newlineremove = request.POST.get('Newlineremove', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    WordCount = request.POST.get('WordCount', 'off')
    removepunc = request.POST.get('removepunc','off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''

    if removepunc != "off":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if fullcaps=='on':
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
       
    if Newlineremove=='on':
        analyzed = ""
        for char in djtext:
           if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
       
    if extraspace =='on':
        analyzed = ""
        for index in range(1,len(djtext)):
            if not(djtext[index-1]== " " and djtext[index]==" "):
                analyzed = analyzed + djtext[index]
        #analyzed = analyzed + djtext[index]
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if WordCount =='on':
        analyzed=0
        for i in range(len(djtext)):
            if djtext[i]!=" " :
                analyzed = analyzed + 1
        params = {'purpose': 'Word Count', 'analyzed_text': [djtext, analyzed] }
        
    if WordCount !='on' and extraspace !='on' and Newlineremove!='on' and fullcaps!='on' and removepunc != "on":
        return HttpResponse("Error found")
    
    return render(request, 'analyze.html', params)


    

    
    







