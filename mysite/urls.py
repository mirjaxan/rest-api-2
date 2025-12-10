from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
		path('', include('api.urls')),
		path('author/', include('author.urls')),
		path('article/', include('article.urls')),
		path('post/', include('post.urls')),
]
9