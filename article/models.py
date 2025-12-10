from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	author = models.CharField(max_length=200)
	content = models.CharField(max_length=200)
	views = models.IntegerField()

	def __str__(self):
		return self.title + self.author 

