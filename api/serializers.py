from pyexpat import model
from rest_framework import serializers
from api.models import Post,Customer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ('first_name', 'last_name', 'username','email',"password","id")

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id','serviceship',"width",'height','length','weight','custumer')

class PostSerializer_customer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"

