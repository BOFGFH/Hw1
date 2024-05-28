from django.shortcuts import render

def getR(request):
    return render(request, "home.html")