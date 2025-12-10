from rest_framework.response import Response 
from rest_framework.decorators import api_view

from .models import Author

@api_view(['GET', 'POST'])
def get_item(request):

	data = Author.objects.all()
	articles = []

	for i in data:
		author = {
				"title": i.bio,
				"atuhor": i.full_name,
				"content": i.created_at,
		}

		articles.append(author)

	if request.method == "POST":
		
		
		return	Response( {
								"status": True,
								"data": articles
							})

	return Response(articles)

@api_view(['GET'])
def author(request, pk):
	
	try:
		artcilce = Author.objects.get(id=pk)
	except Author.DoesNotExist:
		return Response({"Error": "Book does not exists"}, status=404)
	
	data = {
				"title":artcilce.full_name,
				"atuhor": artcilce.created_at,
				"content": artcilce.bio,
	}

	return Response(data)