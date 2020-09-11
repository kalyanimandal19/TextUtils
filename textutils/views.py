from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def contact(request):
     return render(request,'contact_us.html')

def about(request):
     return render(request,'about_us.html')

def analyse(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Checkboxes values
    removepunc =  request.POST.get('removepunc', 'off')
    fullcaps =  request.POST.get('fullcaps', 'off')
    newlineremover =  request.POST.get('newlineremover', 'off')
    extraspaceremover =  request.POST.get('extraspaceremover', 'off')
    charcount =  request.POST.get('charcount', 'off')



    # Check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = " "
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose':'Removed Punctuations','analysed_text':analysed}
        djtext = analysed

    if fullcaps == 'on':
        analysed = " "
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'Changed To Upper Case', 'analysed_text': analysed}
        djtext = analysed

    if newlineremover == 'on':
        analysed = " "
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed = analysed + char
        params = {'purpose': 'New Line Removed', 'analysed_text': analysed}
        djtext = analysed

    if extraspaceremover == 'on':
            analysed = " "
            for index,char in enumerate(djtext):
                if not(djtext[index] == " " and djtext[index+1] == " "):
                    analysed = analysed + char
            params = {'purpose': 'Extra Space Removed', 'analysed_text': analysed}
            djtext = analysed

    if charcount == 'on':
        count = 0
        for char in djtext:
            count = count+1
        params = {'purpose': 'Character Counter', 'analysed_text': djtext,'count': count}

    if removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on':
        message = [djtext,"   Please check atleast one option!"]
        return HttpResponse(message)

    return render(request, 'analyse.html', params)


