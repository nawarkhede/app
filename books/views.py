# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from books.forms import BookAddForm
from authors.models import Author
from books.models import Book
from django.contrib.auth.decorators import login_required


@login_required
def add(request):

	if request.method == 'GET':
		form = BookAddForm()
	else:
		form = BookAddForm(request.POST)
		if form.is_valid():
			id_of_author=form.cleaned_data['author_id']
			name_of_the_book = form.cleaned_data['name']
			author_object = Author.objects.get(id=id_of_author)
			book_object =  Book()
			book_object.name = name_of_the_book
			book_object.author_name = author_object
			book_object.save()
			return HttpResponseRedirect('/landingpage/')



			print author_object.name
	return render(request, 'books/addbook.html', {'addbookform':form})