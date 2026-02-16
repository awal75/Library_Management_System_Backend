from rest_framework_nested import routers
from django.urls import path,include
from library import views


router=routers.DefaultRouter()
router.register(r'books',views.BookModelViewSet,basename='books')
router.register(r'members',views.MemberModelViewSet,basename='members')
router.register(r'authors',views.AuthorModelViewSet,basename='authors')
router.register(r'borrow-records', views.BorrowRecordModelViewSet)


urlpatterns = [
    path('',include(router.urls)),
   
]

