from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
from django.views.generic import DetailView

def news_home(request):
    news = Articles.objects.all()
    return render(request, 'main/index.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'main/details_view.html'
    context_object_name = 'article'

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse('<h4>I will do it later</h4>')
