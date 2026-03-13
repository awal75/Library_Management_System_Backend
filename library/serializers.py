from rest_framework import serializers
from library import models


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Book
        fields = ['id','title','author','ISBN','category','total_copies','available_copies','availability_status']
        read_only_fields = ['id', 'availability_status']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = ['id', 'user', 'biography']


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Member
        fields = ['id', 'user', 'membership_date']


class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BorrowRecord
        fields=['id','borrow_date','return_date']

    def create(self, validated_data):
        member=self.context['member']
        book=self.context['book']

        
        return models.BorrowRecord.objects.create(book=book,member=member,**validated_data)

        
class UpdateBorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BorrowRecord
        fields=['return_date']

class ReturnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BorrowRecord
        fields=['id','book','member','borrow_date','return_date','return_status','actual_return_date']

class ReturnSerializer(serializers.Serializer):
    email=serializers.EmailField()
        