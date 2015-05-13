from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from authors.models import Author

def home(request):
	return render_to_response('index.html', {'posts': ''})


def profile(request):
	 return HttpResponseRedirect('/landingpage/')

def landingpage(request):

	authors_list  = Author.objects.all()
	return render(request, 'landingpage.html', {'authors_list':authors_list})