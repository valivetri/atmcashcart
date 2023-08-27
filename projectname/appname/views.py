from django.shortcuts import render

def index(request):
    return render(request, 'appname/index.html')

def login(request):
    return render(request, 'appname/login.html')

def form(request):
    return render(request, 'appname/form.html')

def count(request):
    return render(request, 'appname/count.html')

def analyze(request):
    return render(request, 'appname/analyze.html')

def final(request):
    return render(request, 'appname/final.html')
