from django.db import models

class Post(models.Model):
    author = models.ForeignKey("author.Author", on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="posts/", blank=True, null=True)

    likes = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)