from .models import Article
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import SearchForm
from .forms import ArticleForm

def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        artilces = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
        'message': 'Hello Django',
        'articles': articles,
        'searchForm': searchForm,
    }
    return render(request, 'bbs/index.html', context)

def detail(request, id):
  article = get_object_or_404(Article, pk=id)
  context = {
    'maseeage': 'Show Article ' + str(id),
    'article': article,
   }
  return render(request, 'bbs/ditail.html', context)

def new(request):
    articleForm = ArticleForm()

    context = {
        'message': 'New Article',
        'articleForm': articleForm,
    }
    return render(request, 'bbs/new.html', context)

def create(request):
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            article = articleForm.save()
    context = {
      'message': 'Create article ' + str(article.id),
      'articles': article,
    }
    return render(request, 'bbs/detail.html', context)

def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    articleForm = ArticleForm(instance=article)

    context = {
        'message': 'Edit Article',
        'articles': articles,
        'articleForm': articleForm,
    }
    return render(request, 'bbs/edit.html', context)

def update(request, id):
    if request.method == 'POSt':
        article = get_object_or_404(Article, pk=id)
        articleForm = ArticleForm(request.POST, instance=article)
        if articleForm.is_valid():
            articleForm.save()

    context = {
        'message': 'Update article ' + str(id),
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)

def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    articles = Article.objects.all()
    context = {
        'message': 'Delete article ' + str(id),
        'articles': articles,
    }
    return render(request, 'bbbs/index.html', context)