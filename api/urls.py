from django.urls import path
from .views import get_item, book_detail

urlpatterns = [
	path("", get_item, name='create'),
	path('book/<int:pk>',book_detail)
]