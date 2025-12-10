from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=150)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_nam
