from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer

def book_list(request):
    books = Book.objects.all()      #get all the books
    serializer = BookSerializer(books, many=True)      #serialize them
    return JsonResponse({"books": serializer.data}, safe=False)        #return json