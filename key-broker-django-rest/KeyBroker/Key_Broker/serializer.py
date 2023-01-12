from rest_framework import serializers

# from student_management_system.studentmanagementsystem.models import Student
from .models import User
from .models import property

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    
    def create(self,validated_data):
        print("check")
        return User.objects.create(**validated_data)


class UserLoginSerializer(serializers.Serializer):    
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    
    def create(self,validated_data):
        print("check")
        return User.objects.create(**validated_data)

class propertySerializer(serializers.Serializer):
    username = serializers.CharField(max_length=250)
    nameofpropery = serializers.CharField(max_length=250)
    nameofuser = serializers.CharField(max_length=250)
    guid = serializers.CharField(max_length=250)
    address = serializers.CharField(max_length=250)
    price = serializers.IntegerField()
    room = serializers.IntegerField()
    size=serializers.IntegerField()
    category=serializers.CharField(max_length=250)
    area=serializers.CharField(max_length=250)
    image1 = serializers.ImageField()
    image2 = serializers.CharField(max_length = 250)
    image3 = serializers.CharField(max_length = 250)
    image4 = serializers.CharField(max_length = 250)
    phoneno= serializers.IntegerField()
    date=serializers.CharField(max_length = 250)
    detail=serializers.CharField(max_length=250)
    id = serializers.IntegerField()
    def create(self,validated_data):
        print("check")
        return property.objects.create(**validated_data)


