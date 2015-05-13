from django.db import models


'''class Book(models.Model):
	name = models.CharField(max_length=20)
	author_name = models.ForeignKey('Author')
'''


class Author(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()

	def __unicode__(self):
		return 'Author : '+self.name