from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article



def blog_page(request):
	return render(request, 'index.html')

def root(request):
    return HttpResponseRedirect('home')


def home(request):
    articles = Article.objects.filter(draft=False).order_by('published_date').all()
    context = {
        'articles': articles
    }
    response = render(request, 'base.html', context)
    return HttpResponse(response)

def title_view(request, id):
	blog = Article.objects.get(pk=id)
	context = {
        'blog': blog,
    }
	response = render(request, 'article.html', context)
	return HttpResponse(response)
