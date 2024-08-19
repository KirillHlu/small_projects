from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles

def news_home(request):
    news = Articles.objects.all()
    return render(request, 'main/index.html', {'news': news})

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse('<h4>I will do it later</h4>')
