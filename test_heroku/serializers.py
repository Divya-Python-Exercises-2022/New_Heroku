from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from test_heroku.models import Book

class BookSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ['url', 'id', 'title']
