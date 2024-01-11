# i have created a file

from django.http import HttpResponse
from django.shortcuts import render




def index(request):

    return render(request, 'index.html')

def analyze(request):

#Get the text
    djtext=request.POST.get('text','default')

#Check Checkbox Value

    removepunc=request.POST.get('removepunc','OFF')
    fullcaps=request.POST.get('fullcaps','OFF')
    newlineremover=request.POST.get('newlineremover','OFF')
    extraspaceremover=request.POST.get('extraspaceremover','OFF')
    charcounter=request.POST.get('charcounter','OFF')


# Check which check box is ON----------------



    if removepunc== "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed +char

        params= {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed


    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to Upper Case', 'analyzed_text': analyzed}
        djtext= analyzed


    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index+1]==" ") :
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Remove', 'analyzed_text': analyzed}
        djtext=analyzed


    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Change to Upper Case', 'analyzed_text': analyzed}
        djtext=analyzed


    if (charcounter == "on"):
        analyzed = ""
        c=0
        for char in djtext:
            if char!= "":
                c=c+1
                analyzed = analyzed + char
        counter ="No of character is: "+ str(c)
        params = {'purpose': 'count number of character', 'analyzed_txt': counter }
        # return render(request, 'analyze.html', dic)
    if (removepunc != "on" and newlineremover !="on" and extraspaceremover != "on" and  fullcaps != "on" and charcounter !="on"):
        return HttpResponse("Please select any operation And Try again")


    return render(request, 'analyze.html', params)

