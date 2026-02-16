from rest_framework import serializers
from library import models


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Book
        fields=['id','title','author','ISBN','category','availability_status']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Author
        fields=['id','name','biography']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Member
        fields=['id','name','email','membership_date']


class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BorrowRecord
        fields=['id','book','member','borrow_date','return_date']
        
class UpdateBorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BorrowRecord
        fields=['return_date']
        