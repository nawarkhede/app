from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from authors.forms import AuthorAddForm
from authors.models import Author
from django.contrib.auth.decorators import login_required


@login_required
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
			return HttpResponseRedirect('/landingpage/')
	return render(request, 'authors/addauthor.html', {'addauthorform':form})