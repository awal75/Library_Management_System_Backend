from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from library import serializers
from library import models
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
    serializer_class=serializers.BorrowRecordSerializer
    queryset=models.BorrowRecord.objects.all()