from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(max_length=250)
	body = models.TextField()
	draft = models.BooleanField()
	published_date = models.DateField()
	author = models.CharField(max_length=250)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
	
	def __str__(self):
		return self.title