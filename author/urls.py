from django.urls import path
from .views import get_item, author

urlpatterns = [
	path("", get_item, name='create'),
	path('author/<slug:slug>', author)
]