from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from authors.models import Author
from books.models import Book

def home(request):
	return HttpResponseRedirect('/landingpage/')


def profile(request):
	 return HttpResponseRedirect('/landingpage/')

def landingpage(request):

	# authors_list  = Author.objects.all()
	# books_list = Book.objects.all()
	return render(request, 'landingpage.html', {'authors_list':'','books_list':''})