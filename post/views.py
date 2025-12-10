from rest_framework.response import Response 
from rest_framework.decorators import api_view

from .models import Post

@api_view(['GET', 'POST'])
def get_item(request):

	data = Post.objects.all()
	articles = []

	for i in data:
		data	 = {
				"title": i.title,
				"author": i.author,
				"content": i.content,
				"likes": i.likes,
				"is_published": i.is_published,
		}

		articles.append(data)

	if request.method == "POST":
		
		
		return	Response( {
								"status": True,
								"data": articles
							})

	return Response(articles)

@api_view(['GET'])
def post_detail(request, pk):
	
	try:
		artcilce = Post.objects.get(id=pk)
	except Post.DoesNotExist:
		return Response({"Error": "Posts does not exists"}, status=404)
	
	data = {
				"title":artcilce.title,
				"author": artcilce.author,
				"content": artcilce.content,
				"likes": artcilce.likes,
				"is_published": artcilce.is_published,
	}

	return Response(data)