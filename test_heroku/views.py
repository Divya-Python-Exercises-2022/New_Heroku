from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from test_heroku.models import Book
from test_heroku.serializers import BookSerializer

# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookApiView(APIView):

    def get(self, request: Request):
        #logger.info('Get Received...')

        return Response({'message':'Hi from Book'}, status=status.HTTP_200_OK)
