from . import views
from django.urls import path, include,re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
urlpatterns = [
    path('ttt/',views.index, name='index'),
    path('', include(router.urls)),
]


