from django.shortcuts import render

from django.http import HttpResponse
from polls.models import Choice, Poll
from blog.models import Artigo
from django.template import Context, loader


def index2(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request,'index.html', {'latest_poll_list': latest_poll_list})

def index22(request):
    latest_choice_list = Choice.objects.all()
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render(request,'index2.html', {'latest_choice_list': latest_choice_list, 'latest_poll_list': latest_poll_list}, )

def index(request):
	return render(request, 'index.html')