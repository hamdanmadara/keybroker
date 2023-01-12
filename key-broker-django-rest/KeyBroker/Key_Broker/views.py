import dataclasses
import imp
import json
from urllib import response
import MySQLdb
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import mysqlx
from .models import User, property
from .serializer import UserLoginSerializer, UserSerializer, propertySerializer

from django.db import connections

# from rest_framework.views import APIView

from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from time import gmtime, strftime
# Create your views here.

@api_view(['GET','POST'])
def user(request):
    if request.method == "GET":
        user = User.objects.raw("select * from key_broker_usertable")
        serializer = UserSerializer(user , many=True)
        return Response(serializer.data)

    if request.method == "POST":
        # user123 = User.objects.raw("select * from user")
        # user12 = User.objects.raw("select * from user")
        # print(user123,user12)
        pythondata = JSONParser().parse(request)
        
        signupserializer = UserSerializer(data=pythondata)
        print(pythondata['username'])
        username=str(pythondata['username'])
        password=str(pythondata['password'])
        loginserializer = UserLoginSerializer(data=pythondata)
        print(222222222222222222)
        print(loginserializer)
        print(222222222222222222)
        check_login=False
        check_signup=False
        cursor = connections['default'].cursor()
        if signupserializer.is_valid():
            user = User.objects.raw("select * from key_broker_usertable where username =%s" , [username])
            if user:
                check_signup = True
                return Response("username already exist")
            
            if check_signup == False:
                print('yes')
                # user = User(first_name=signupserializer.data['first_name'], last_name=signupserializer.data['last_name'], email=signupserializer.data['email'], username=signupserializer.data['username'], password=signupserializer.data['password'])
                # user.save()
                cursor.execute("INSERT INTO key_broker_usertable(first_name,last_name,email,username,password) VALUES( %s , %s, %s, %s, %s  )"
                , [signupserializer.data['first_name'],signupserializer.data['last_name'],signupserializer.data['email'],signupserializer.data['username'],signupserializer.data['password']])
                print('yesssssss')
                
            
                return Response("account create successfully")
            
        if loginserializer.is_valid():            
            print(loginserializer.data['username'])
            user = User.objects.raw("select * from key_broker_usertable")
            user1 = User.objects.raw("select * from key_broker_usertable where username =%s AND password =%s" , [username,password])

            if user1:
                print("aaaaaaaaaaaaa")
                check_login = True
                return Response("proceed")
            
            if check_login == False:
                print("bbbbbbbbb")
                return Response("Wrong Credentials")


@api_view(['GET','POST'])
def uploadProperty(request):
    if request.method == "GET":
        property1 = property.objects.raw("select * from property")
        serializer = propertySerializer(property1 , many=True)
        print(serializer)
        return Response(serializer.data)


    if request.method == "POST":
        
        
        # property1 = upload_property.objects.raw("select * from key_broker_upload_property")
        # print(st)
        # user123 = User.objects.raw("select * from user")
        # user12 = User.objects.raw("select * from user")
        # print(user123,user12)
        showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        pythondata = JSONParser().parse(request)

    #     username:this.username,
    #   fullName: this.fullName,
    #   propertyName: this.propertyName,
    #   address: this.address,
    #   datail: this.detail,
    #   imgUrl1: this.imageUrl1,
    #   imgUrl2: this.imageUrl2,
    #   imgUrl3: this.imageUrl3,
    #   imgUrl4: this.imageUrl4,
    #   area: this.areaName,
    #   category: this.categoryName,
    #   size: this.size,
    #   room: this.room,
    #   price: this.price,
    #   phoneNo: this.phoneNo

        
        username=str(pythondata['username'])
        propertyname=str(pythondata['propertyName'])
        nameofuser=str(pythondata['fullName'])
        guid=str(pythondata['username'])
        address=str(pythondata['address'])
        price=str(pythondata['price'])
        room=str(pythondata['room'])
        propertysize=str(pythondata['size'])
        category=str(pythondata['category'])
        area=str(pythondata['area'])
        img1=str(pythondata['imgUrl1'])
        img2=str(pythondata['imgUrl2'])
        img3=str(pythondata['imgUrl3'])
        img4=str(pythondata['imgUrl4'])
        phoneno=str(pythondata['phoneNo'])
        date=showtime
        detail=str(pythondata['datail'])
        
        
        # loginserializer = UserLoginSerializer(data=pythondata)
        
        cursor = connections['default'].cursor()
        # cursor.execute("INSERT INTO key_broker_upload_property(name_of_property,name_of_user,guid,address,price,rooms,property_size,catagory,image1,image2,image3,image4,phone_no,date,datail) VALUES( %s, %s, %s, %s, %s , %s, %s, %s, %s, %s , %s, %s, %s, %s, %s  )"
        #         , [propertyname,nameofuser,guid,address,price,room,propertysize,category,img1,img2,img3,img4,phoneno,date,detail])
        # st=upload_property.objects.all()
        cursor.execute("INSERT INTO property(username,nameofpropery,nameofuser,guid,address,price,room,size,category,area,image1,image2,image3,image4,phoneno,date,detail) VALUES( %s, %s, %s, %s, %s , %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s  )"
                , [username,propertyname,nameofuser,guid,address,price,room,propertysize,category,area,img1,img2,img3,img4,phoneno,date,detail])
        # st=upload_property.objects.all()
        # property1 = upload_property.objects.raw("select * from key_broker_upload_property")
        return Response("inserted")   


@api_view(['GET','POST'])
def buyerForm(request):
    if request.method == "GET":
        # mycursor = mydb.cursor()
        mycursor = connections['default'].cursor()

        mycursor.execute("SELECT * FROM key_broker_interested_user")

        myresult = mycursor.fetchall()
        print(myresult)
        # property1 = property.objects.raw("select * from property")
        # serializer = propertySerializer(property1 , many=True)
        # print(serializer)
        return Response(myresult)


    if request.method == "POST":
        
        
        # property1 = upload_property.objects.raw("select * from key_broker_upload_property")
        # print(st)
        # user123 = User.objects.raw("select * from user")
        # user12 = User.objects.raw("select * from user")
        # print(user123,user12)
        showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        pythondata = JSONParser().parse(request)

    #     username:this.username,
    #   fullName: this.fullName,
    #   propertyName: this.propertyName,
    #   address: this.address,
    #   datail: this.detail,
    #   imgUrl1: this.imageUrl1,
    #   imgUrl2: this.imageUrl2,
    #   imgUrl3: this.imageUrl3,
    #   imgUrl4: this.imageUrl4,
    #   area: this.areaName,
    #   category: this.categoryName,
    #   size: this.size,
    #   room: this.room,
    #   price: this.price,
    #   phoneNo: this.phoneNo

        
        name=str(pythondata['name'])
        phoneNo=str(pythondata['phoneNo'])
        propertyId=str(pythondata['propertyId'])
        
        
        # loginserializer = UserLoginSerializer(data=pythondata)
        
        cursor = connections['default'].cursor()
        # cursor.execute("INSERT INTO key_broker_upload_property(name_of_property,name_of_user,guid,address,price,rooms,property_size,catagory,image1,image2,image3,image4,phone_no,date,datail) VALUES( %s, %s, %s, %s, %s , %s, %s, %s, %s, %s , %s, %s, %s, %s, %s  )"
        #         , [propertyname,nameofuser,guid,address,price,room,propertysize,category,img1,img2,img3,img4,phoneno,date,detail])
        # st=upload_property.objects.all()
        cursor.execute("INSERT INTO key_broker_interested_user(name_of_user,property_guid,phone_no,date) VALUES( %s, %s, %s, %s  )"
                , [name,propertyId,phoneNo,showtime])
        # st=upload_property.objects.all()
        # property1 = upload_property.objects.raw("select * from key_broker_upload_property")
        return Response("inserted")   



@api_view(['GET','POST'])
def deleteProperty(request):
    # if request.method == "GET":
    #     property1 = property.objects.raw("select * from property")
    #     serializer = propertySerializer(property1 , many=True)
    #     print(serializer)
    #     return Response(serializer.data)


    if request.method == "POST":
        pythondata = JSONParser().parse(request)
        id1=pythondata['id']
        print(id1)
        cursor = connections['default'].cursor()
        cursor.execute('DELETE FROM property WHERE id = %s',(str(id1), ))
        return Response("deleted")


@api_view(['GET','POST'])
def deleteBuyer(request):
    # if request.method == "GET":
    #     property1 = property.objects.raw("select * from property")
    #     serializer = propertySerializer(property1 , many=True)
    #     print(serializer)
    #     return Response(serializer.data)


    if request.method == "POST":
        pythondata = JSONParser().parse(request)
        id1=pythondata['id']
        print(id1)
        cursor = connections['default'].cursor()
        cursor.execute('DELETE FROM key_broker_interested_user WHERE property_guid = %s',(str(id1), ))
        return Response("deleted")
       
    
    



