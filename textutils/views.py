from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def analyzer(request):
    text = request.POST.get("text", "default")
    removepunc = request.POST.get("removepunc", "off")
    newlineremove = request.POST.get("newlineremove", "off")
    extraspaceremove = request.POST.get("extraspaceremove", "off")
    upper = request.POST.get("upper", "off")
    lower = request.POST.get("lower", "off")
    charcount = request.POST.get("charcount", "off")
    capfirst = request.POST.get("capfirst", "off")
    purpose = ""
    analyzetext = text

    if removepunc == "on":
        actions = "|Remove Punctuation|"
        pretext = ""
        punctuations = '''!@#$%^&*()\{\}?<>"':;`|[]-'''
        for char in analyzetext:
            if char not in punctuations:
                pretext += char
        purpose += actions
        analyzetext = pretext

    if newlineremove == "on":
        pretext = ""
        for char in analyzetext:
            if char != "\n" and char == "\r":
                pretext += char
        purpose += "|New Line Character Remove|"
        analyzetext = pretext

    if extraspaceremove == "on":
        pretext = ""
        for index, char in enumerate(analyzetext):
            if not(analyzetext[index] == " " and analyzetext[index+1] == " " or analyzetext[index] == "\n"):
                pretext += char
        purpose += "|Extra Space Remove|"
        analyzetext = pretext

    if upper == "on":
        analyzetext = analyzetext.upper()
        purpose += "|UPPERCASE|"

    if lower == "on":
        analyzetext = analyzetext.lower()
        purpose += "|lowercase|"

    if charcount == "on":
        analyzetext += f"\n------------------# {len(analyzetext)} Characters"
        purpose += "|Character Count|"
    
    if capfirst == "on":
        analyzetext = analyzetext.capitalize()
        purpose += "|Capitalize|"
    
    if newlineremove == "on" or extraspaceremove == "on" or removepunc == "on" or upper == "on" or lower == "on" or charcount == "on" or capfirst == "on":
        params = {"actions": purpose, "analyze_text": analyzetext}
        return render(request, "analyze.html", params)
    else:
        return render(request, "index.html")
# def charcount(request):
#     return HttpResponse("charcount")

# def newlineremove(request):
#     return HttpResponse("newlineremove")

# def spaceremove(request):
#     return HttpResponse("spaceremove")

# def removepunc(request):
#     text = request.POST.POST("text", "default")
#     return HttpResponse("removepunc")

# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst")
