from django.urls import path
from .views import *
from rest_framework_simplejwt.views import *

urlpatterns = [
    path('', index, name='home'),
    path('api/token', TokenObtainPairView.as_view()),
]