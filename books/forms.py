from django import forms
from authors.models import Author



def get_all_authors():
	all_authors=[]
	for i in Author.objects.all():
		all_authors.append((i.id,i.name))
	return all_authors

class BookAddForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(BookAddForm, self).__init__(*args, **kwargs)
		self.fields['author_id'] =forms.ChoiceField(choices=get_all_authors())
		print dir(self)
	name = forms.CharField()
	author_id = forms.ChoiceField(choices=get_all_authors())

