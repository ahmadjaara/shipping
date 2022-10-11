from rest_framework import generics
from api.models import Post,Customer
from .serializers import PostSerializer,PostSerializer_customer,UserSerializer
from django.contrib.auth.models import User

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
     

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class Customerdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Customer.objects.all()
    serializer_class=UserSerializer

class CustomerdetailList(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer