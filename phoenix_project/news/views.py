from django.shortcuts import redirect, render

from .forms import *
from .models import *


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Latest news',
        'categories': categories
    }
    return render(
        request,
        template_name='news/index.html',
        context=context
    )

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'title': 'Latest news',
        'categories': categories,
        'category': category
    }
    return render(
        request,
        template_name='news/category.html',
        context=context
    )

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('homepage')
        else:
            print('Errors in form')
    else:
        form = NewsForm()
    return render(
        request,
        'news/add_news.html',
        {'form': form}
    )
