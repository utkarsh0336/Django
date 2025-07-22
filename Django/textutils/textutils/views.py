from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name' : 'Utkarsh' , 'place' : 'Bengaluru'}
    return render(request, 'index.html',params)

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #Check checkbox values
    removepunc = request.POST.get('removepunc' , 'off')   # .get() takes 1 parameter as name='' (given in the HTML code) and 2 parameter as default value.
    fullcaps = request.POST.get('fullcaps' , 'off')
    newlineremover = request.POST.get('newlineremover' , 'off')
    extraspaceremover = request.POST.get('extraspaceremover' , 'off')

    #Check which checkbox is on 
    if removepunc == 'on':
        punctuation = r""".,!?;:'"-–—()[]{}…/\@#$%&*^_~|<>="""
        analyzed = ""
        for ch in djtext:
            if ch not in punctuation:
                analyzed = analyzed + ch
        params = {'purpose' : 'Removed Punctuation' , 'analysed_text' : analyzed}
        djtext = analyzed
    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Changed to Uppercase' , 'analysed_text' : analyzed}
        djtext = analyzed
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose' : 'Removed New Line Character' , 'analysed_text' : analyzed}
        djtext = analyzed
    if(extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if index < len(djtext) - 1 and not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
                
        params = {'purpose' : 'Removed Extra Space' , 'analysed_text' : analyzed}
        djtext = analyzed
    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Please Select any Operation and Try Again !!")
    
    return render(request,'analyze.html',params)





    