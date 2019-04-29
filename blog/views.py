from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article
from blog.forms import LoginForm, articleform
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


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


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()

    context = {'form': form}
    http_response = render(request, 'login.html', context)
    return HttpResponse(http_response)
    
    #registered = False

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice :)")
    
@login_required
def logout_view(request):
    logout(request)
    return(HttpResponseRedirect('/home/'))


def article_view(request):
    if request.method == 'POST':
        form = articleform(request.POST)
        if form.is_valid():
                add_form = form.save(commit=False)
                add_form.save()
                return redirect('')
        else:
            form = articleform()
    else: 
        form = articleform()
    return render(request, 'articlepost.html', {'form':form})
