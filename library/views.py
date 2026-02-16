
from rest_framework.viewsets import ModelViewSet
from library import serializers
from library import models
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.utils import timezone
# Create your views here.


class BookModelViewSet(ModelViewSet):
    serializer_class=serializers.BookSerializer
    queryset=models.Book.objects.all()



class MemberModelViewSet(ModelViewSet):
    serializer_class=serializers.MemberSerializer
    queryset=models.Member.objects.all()


class AuthorModelViewSet(ModelViewSet):
    serializer_class=serializers.AuthorSerializer
    queryset=models.Author.objects.all()
    
   


class BorrowRecordModelViewSet(ModelViewSet):
    http_method_names=['get','post','patch','delete']
    queryset=models.BorrowRecord.objects.all()

    def get_serializer_class(self):
        if self.request.method=='PATCH':
            return serializers.UpdateBorrowRecordSerializer
        return serializers.BorrowRecordSerializer

    
