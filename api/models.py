from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=100)
	slug  = models.SlugField(max_length=100, unique=True)
	content = models.TextField()
	publish_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
	
	