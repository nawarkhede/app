from django.db import models
from authors.models import Author
# Create your models here.

class Book(models.Model):
	name = models.CharField(max_length=20)
	author_name = models.ForeignKey(Author)

	def __unicode__(self):
		return 'Book : '+self.name