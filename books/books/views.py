from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()      #get all the books
        serializer = BookSerializer(books, many=True)      #serialize them
        return JsonResponse({"books": serializer.data}, safe=False)        #return json

    if request.method == 'POST':
        #take the data you got
        #de-serialize it
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    