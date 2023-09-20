from django.db import models
import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Customers(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    contact=models.CharField(max_length=10)

class Plants(models.Model):
    
    category_choices=(
        ("zodiac","Zodiac"),
        ("flowering","Flowering"),
        ("low_maintain","Low_Maintenance"),
        ("medicinal","Medicinal"),
        ("air_purifying","Air_Purifying"),
        ("pet-friendly","Pet-Friendly")
    )

    subcategory_choices=(
        ("indoor","Indoor"),
        ("outdoor","Outdoor")
    )

    size_choices=(
        ("large","Large"),
        ("medium","Medium"),
        ("small","Small"),
    )
    
   
    plant_name=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)
    size=models.CharField(max_length=50, choices=size_choices)
    family=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.CharField(max_length=50, choices=category_choices, null=True)   
    sunlight=models.CharField(max_length=1000, null=True)
    water=models.CharField(max_length=1000, null=True)
    fertilizer=models.CharField(max_length=1000, null=True)
    temperature=models.CharField(max_length=100,default="")
    subcategory=models.CharField(max_length=50,choices=subcategory_choices,default="Indoor", null=True)
    images=models.ImageField(upload_to="plants/images", default="",null=True, blank=True)

    def __str__(self) -> str:
        return self.plant_name

class Products(models.Model):
    main_choices = (
        ("fertilizer", "Fertilizers"),
        ("tool", "Tools"),
        ("pot", "Pots"),

    )
    size_choices=(
        ("large","Large"),
        ("medium","Medium"),
        ("small","Small"),
    )
    mainCategory = models.CharField(max_length=100, choices=main_choices, default="Fertilizers")
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    
    size = models.CharField(max_length=50, choices=size_choices)
    images = models.ImageField(upload_to="products/images", default="", null=True, blank=True)

    def __str__(self):
        return self.product_name


    
class WishList(models.Model):

    customerId=models.ForeignKey(Customers,on_delete=models.CASCADE)
    plantId=models.ForeignKey(Plants,on_delete=models.CASCADE,null=True)
    likedPlants=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.customerId} : {self.plantId}"
    class Meta:
        # Define unique_together as a list of tuples specifying unique combinations of fields
        unique_together = [['customerId', 'plantId']]

class WishListProduct(models.Model):
    
    customerId=models.ForeignKey(Customers,on_delete=models.CASCADE)
    productId=models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    likedProducts=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.customerId} : {self.productId}"
    class Meta:
        # Define unique_together as a list of tuples specifying unique combinations of fields
        unique_together = [['customerId', 'productId']]

class Orders(models.Model):
   plant = models.ForeignKey(Plants,on_delete=models.CASCADE)
   customer=models.ForeignKey(Customers,on_delete=models.CASCADE)
   #product=models.ForeignKey(Products,on_delete=models.CASCADE)
   quantity=models.IntegerField(default=1)
   price=models.IntegerField()
#    address=models.CharField(max_length=100)
#    phone=models.CharField(max_length=10)
#    date=models.DateField(default=datetime.datetime.today)
#    status=models.BooleanField(default=False)
class Cart(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)  # Add this field

    def __str__(self):
        return f'{self.user.username} - {self.content_object}'