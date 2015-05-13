

from django import forms

class AuthorAddForm(forms.Form):
	name = forms.CharField()
	email =forms.EmailField()


