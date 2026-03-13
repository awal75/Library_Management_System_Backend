from rest_framework_nested import routers
from django.urls import path,include
from .views import CustomizeUserViewSet

router=routers.DefaultRouter()
router.register('users',CustomizeUserViewSet,basename='users')

urlpatterns = [
    path('',include(router.urls))
]
