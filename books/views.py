from django.http import HttpResponse
from django.shortcuts import render
from books.forms import AuthorAddForm
from books.models import Author

def add(request):

	if request.method == 'GET':
		form = AuthorAddForm()
	else:
		form = AuthorAddForm(request.POST)
		if form.is_valid():
			author=Author()
			author.name = form.cleaned_data['name']
			author.email = form.cleaned_data['email']
			author.save()
	return render(request, 'books/addbook.html', {'addauthorform':form})