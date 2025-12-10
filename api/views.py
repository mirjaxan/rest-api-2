from rest_framework.response import Response 
from rest_framework.decorators import api_view

from .models import Book

@api_view(['GET', 'POST'])
def get_item(request):

	data = Book.objects.all()
	students = []

	for i in data:
		users = {
				"title": i.title,
				"content": i.content,
				"publish_data": i.publish_date
		}

		students.append(users)

	if request.method == "POST":
		
		
		return	Response( {
								"status": True,
								"data": students
							})

	return Response(students)

@api_view(['GET'])
def book_detail(request, pk):
	try:
		book = Book.objects.get(id=pk)
	except Book.DoesNotExist:
		return Response({"Error": "Book does not exists"}, status=404)
	
	data = {
		"id": book.id,
		"title": book.title,
		"content": book.content,
		"publish_date" : book.publish_date
	}

	return Response(data)