from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as BaseUserSerializer
from rest_framework import serializers
from library.models import Author
from djoser.serializers import UserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields=('id','first_name','last_name','email','password','address','phone_number')


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name='customusercreateserializer'
        fields=('id','email','first_name','last_name','phone_number','address')



class AuthorSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta :
        model=Author
        fields=['id','user','biography']
        