from django.shortcuts import render

from django.http import HttpResponse
from blog.models import Artigo
from django.template import Context, loader

def index(request):
    latest_blog_list = Artigo.objects.all().order_by('-pub_date')[:5]
    return render(request,'artigo.html', {'latest_blog_list': latest_blog_list})

