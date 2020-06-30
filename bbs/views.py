from .models import Article
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
    articles = Article.objects.all()
    context = {
        'message': 'Welcome my BBS',
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context)

def detail(request, id):
  article = get_object_or_404(Article, pk=id)
  context = {
    'maseeage': 'Show Article ' + str(id),
    'article': article,
  }
  return render(request, 'bbs/ditail.html', context)

  # def create(request):
  #   article = Aricle(content= 'Hello BBS', user_name='paiza' )
  #   article.save()

  #   articles = Article.objects.all()
  #   context = {
  #     'message': 'Create article',
  #     'articles': articles,
  #   }
  #   return render(request, 'bbs/index.html', context)