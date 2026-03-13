from django.shortcuts import render
from djoser import views
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from library.models import Author
from users.serializers import AuthorSerializer
from rest_framework.response import Response
User=get_user_model()


class CustomizeUserViewSet(views.UserViewSet):

    @action(detail=False,methods=['get'],permission_classes=[IsAuthenticated])
    def authors(self,request):
        
        authors=Author.objects.select_related('user').all()
        serializer=AuthorSerializer(authors,many=True)
        print(serializer.data,'fdsfsd')
        return Response(serializer.data,status=200)
    def perform_create(self, serializer, *args, **kwargs):
        
        return super().perform_create(serializer, *args, **kwargs)
