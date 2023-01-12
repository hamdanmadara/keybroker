from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name

class Admin(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name

class Usertable(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name

# class upload_property(models.Model):
#     username = models.CharField(max_length=250)
#     name_of_property = models.CharField(max_length=250)
#     name_of_user = models.CharField(max_length=250)
#     guid = models.CharField(max_length=250)
#     address = models.CharField(max_length=250)
#     price = models.IntegerField()
#     rooms = models.IntegerField()
#     property_size=models.IntegerField()
#     catagory=models.CharField(max_length=250)
#     Area=models.CharField(max_length=250)
#     image1 = models.ImageField()
#     image2 = models.ImageField()
#     image3 = models.ImageField()
#     image4 = models.ImageField()
#     phone_no= models.IntegerField()
#     date=models.DateField()
#     datail=models.CharField(max_length=250)
    
    
#     def __str__(self):
#         return self.name_of_user

class property(models.Model):
    username = models.CharField(max_length=250)
    nameofpropery = models.CharField(max_length=250)
    nameofuser = models.CharField(max_length=250)
    guid = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    price = models.IntegerField()
    room = models.IntegerField()
    size=models.IntegerField()
    category=models.CharField(max_length=250)
    area=models.CharField(max_length=250)
    image1 = models.ImageField()
    image2 = models.CharField(max_length = 250)
    image3 = models.CharField(max_length = 250)
    image4 = models.CharField(max_length = 250)
    phoneno= models.IntegerField()
    date=models.CharField(max_length = 250)
    detail=models.CharField(max_length=250)
    # id = models.IntegerField()
    
    
    def __str__(self):
        return self.username


# class interested_user(models.Model):
#     username = models.CharField(max_length=250)
#     name_of_user = models.CharField(max_length=250)
#     property_guid = models.CharField(max_length=250)
#     phone_no= models.IntegerField()
#     date=models.DateField()
    
#     def __str__(self):
#         return self.name_of_user

class Soled_houses(models.Model):
    
    property_guid = models.CharField(max_length=250)
    buyer_name = models.CharField(max_length=250)
    saler_name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name_of_user

