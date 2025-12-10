from rest_framework.response import Response 
from rest_framework.decorators import api_view

from .models import Article

@api_view(['GET', 'POST'])
def get_item(request):

	data = Article.objects.all()
	articles = []

	for i in data:
		art = {
				"title": i.title,
				"atuhor": i.author,
				"content": i.content,
				"views": i.views
		}

		articles.append(art)

	if request.method == "POST":
		
		
		return	Response( {
								"status": True,
								"data": articles
							})

	return Response(articles)

@api_view(['GET'])
def article_detail(request, pk):
	try:
		artcilce = Article.objects.get(id=pk)
	except Article.DoesNotExist:
		return Response({"Error": "Book does not exists"}, status=404)
	
	data = {
				"title":artcilce.title,
				"atuhor": artcilce.author,
				"content": artcilce.content,
				"views": artcilce.views
	}

	return Response(data)