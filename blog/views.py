# Create your views here.
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import  RequestContext
from .models import Article


def index(request):
	articles = Article.objects.all()
	return render_to_response('blog/index.html',{ 'articles': articles },RequestContext(request))


def single(request, article_id):
	article = Article.objects.get(pk=article_id)
	return render_to_response('blog/single.html',{ 'article': article },RequestContext(request))