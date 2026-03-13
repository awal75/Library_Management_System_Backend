
from rest_framework.viewsets import ModelViewSet
from library import serializers
from library import models
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,DjangoModelPermissionsOrAnonReadOnly
from library.service import BookService
from library.permissions import IsLibrarian


class BookModelViewSet(ModelViewSet):
    queryset=models.Book.objects.all()
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]


    @action(detail=True,methods=['post'],permission_classes = [IsAuthenticated])
    def borrow(self,request,pk=None):
        borrow= BookService.borrow_book(book_id=pk,member=request.user.member,return_date=request.data.get('return_date'))
        serializer = self.get_serializer(borrow)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    @action(detail=True,methods=['post'],url_path='return',permission_classes=[IsLibrarian])
    def return_book(self,request,pk=None):
        print(request.data)
        return_bk=BookService.return_book(book_id=pk,email=request.data.get('email'))
        serializer=serializers.ReturnBookSerializer(return_bk)
        return Response(serializer.data,status=status.HTTP_200_OK)


    # def get_permissions(self):
    #     if self.action in ['create','update','destroy','return_book']:
    #         return [IsAuthenticated(),IsAdminUser()]
    #     elif self.action == 'borrow':
    #         return [IsAuthenticated()]
        
    #     else:
    #         return [AllowAny()]
        
    def get_serializer_class(self):
        if self.action=='borrow':
            return serializers.BorrowRecordSerializer
        if self.action == 'return_book':
            return serializers.ReturnSerializer
        return serializers.BookSerializer
        



    
