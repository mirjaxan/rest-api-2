from django.urls import path
from .views import get_item, post_detail

urlpatterns = [
	path("", get_item, name='create'),
	path('post/<slug:slug>', post_detail)
]