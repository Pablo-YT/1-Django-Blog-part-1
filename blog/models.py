from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=250)
	body = models.TextField()
	draft = models.BooleanField()
	published_date = models.DateField()
	author = models.CharField(max_length=250)

	def __str__(self):
		return self.title