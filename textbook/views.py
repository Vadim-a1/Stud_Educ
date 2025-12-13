from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    ##return render(request, 'textbook/index.html')
    return render(request, 'textbook/index.html')

def lectures(request):
    return render(request, 'textbook/lectures.html')

def tests(request):
    return render(request, 'textbook/tests.html')

