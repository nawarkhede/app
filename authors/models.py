from django.db import models


class Author(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()

	def __unicode__(self):
		return 'Author : '+self.name