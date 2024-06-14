from django.shortcuts import render
from news.models import Articles


# Create your views here.
def index(request):
    articles = Articles.objects.order_by('-date')[:3]  # Получаем три последние новости
    return render(request, 'main/index.html', {'articles': articles})

def contacts(request):
    return render(request, 'main/contacts.html')
def news_home(request):
    return render(request, 'news/templates/news/news_home.html')

