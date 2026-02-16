from rest_framework_nested import routers
from django.urls import path,include
from library import views


router=routers.DefaultRouter()
router.register(r'books',views.BookModelViewSet,basename='books')
router.register(r'members',views.MemberModelViewSet,basename='members')
router.register(r'authors',views.AuthorModelViewSet,basename='authors')

book_author=routers.NestedDefaultRouter(router,'books',lookup='book_pk')
book_author.register(r'authors',views.AuthorModelViewSet,basename='book-author')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(book_author.urls)),
]

