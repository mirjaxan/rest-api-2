from django.urls import path
from .views import get_item, article_detail

urlpatterns = [
	path("", get_item, name='create'),
	path('article/<slug:slug>', article_detail)
]