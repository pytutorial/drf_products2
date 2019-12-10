from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['GET'])
def index(request):
    return Response({'message': 'Hello'})

@api_view(['POST'])
def createUser(request):
    username = request.data.get('username')
    password = request.data.get('password')
    errors = []
    if len(password) < 6:
        errors.append('Mật khẩu quá ngắn')
    if User.objects.filter(username=username):
        errors.append('Tên đăng nhập đã tồn tại')
    if username.strip() == '':
        errors.append('Tên đăng nhập không được trống')    
    if len(errors) == 0:
        User.objects.create_user(username=username, password=password)
        return Response({'success' : True})
    else:
        return Response({'success': False, 'errors' : errors})

from .serializers import *
@api_view(['POST'])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success' : True})
    else:
        return Response({'success': False, 'errors': serializer.errors})

from .models import *
@api_view(['GET'])
def getCategoryList(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)