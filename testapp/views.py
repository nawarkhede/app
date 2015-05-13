from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect

def home(request):
	return render_to_response('index.html', {'posts': ''})


def profile(request):
	 return HttpResponseRedirect('/landingpage/')

def landingpage(request):
	 return render(request, 'landingpage.html', {'':''})