from .models import Articles
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from .forms import ArticlesForm
from django.contrib.auth.decorators import login_required


def news_home(request):
    news = Articles.objects.all()
    return render(request, 'main/index.html', {'news': list(reversed(news))})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'main/details_view.html'
    context_object_name = 'article'

def index(request):
    return render(request, 'main/index.html')

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # Привязываем статью к текущему пользователю
            article.save()  # Сохраняем статью
            return redirect('news-home')  # Перенаправление на список статей
    else:
        form = ArticlesForm()
    return render(request, 'main/create_article.html', {'form': form})
