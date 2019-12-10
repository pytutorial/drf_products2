from django.urls import path
from .views import *
from rest_framework_simplejwt.views import *

urlpatterns = [
    path('', index, name='home'),
    path('create_user', createUser),
    path('api/token', TokenObtainPairView.as_view()),
    path('create_category', createCategory),
    path('get_category_list', getCategoryList),
]