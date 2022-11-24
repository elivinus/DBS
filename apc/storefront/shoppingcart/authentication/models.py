from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length= 200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length= 300)
    image = models.ImageField(upload_to='MEDIA_URL', blank=True, null=True)
    category = models.ManyToManyField('Category', related_name = 'MenuItem')
    alergies = models.CharField(max_length= 200, blank=True)

    
    def __str__(self):
         return self.name
 
    @property
    def imageURL(self):
        try:
            url =self.image.url
        except:
            url = ''
        return url


class Category(models.Model):
    name = models.CharField(max_length= 100)
        
    def __str__(self):
        return self.name

class Order(models.Model):
    orderDate = models.DateTimeField(auto_now_add=True)
    totalAmount = models.FloatField()
    orderStatus = models.CharField(max_length=50)
    createDate = models.DateTimeField(auto_now_add=True)
    transactionId = models.CharField(max_length=50,null=True)
    customerId = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    deliveryAgentId = models.ForeignKey('DeliveryAgent', on_delete=models.SET_NULL, null=True, blank=True)
    staffId = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, blank=True)
    paymentStatus = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length= 200, null=True)
    emailaddress = models.EmailField(max_length= 50, null=True)
    phoneNumber = models.IntegerField()
    homeAddress = models.CharField(max_length= 200)
    city = models.CharField(max_length= 200, null=True)
    postcode = models.CharField(max_length= 200, null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    userPassword = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name
    
class DeliveryAgent(models.Model):
    name = models.CharField(max_length= 200)
    emailAddress = models.EmailField()
    phoneNumber = models.IntegerField()
    homeAddress = models.CharField(max_length= 200)
    city = models.CharField(max_length= 200)
    postcode = models.CharField(max_length= 200)
    createDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length= 200)
    emailAddress = models.EmailField(max_length= 200)
    phoneNumber = models.IntegerField()
    homeAddress = models.EmailField()
    city = models.CharField(max_length= 200)
    postcode = models.CharField(max_length= 200)
    createDate = models.DateTimeField(auto_now_add=True)
    userPassword = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class OrderDetail(models.Model):
    quantity = models.IntegerField(default=0, null=True, blank=True)
    totalAmount = models.FloatField(default=0.0, null=True, blank=True)
    createDate = models.DateTimeField(auto_now_add=True)
    menuItemId = models.ForeignKey('MenuItem',on_delete=models.CASCADE, null=True, blank=True)
    orderId = models.ForeignKey('Order', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.totalAmount
    
class Ingredint(models.Model):
    name = models.CharField(max_length= 200)
    price = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    recipeId = models.ForeignKey('Recipe', on_delete=models.CASCADE, null=True, blank=True)
    supplierId = models.ForeignKey('Supplier', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length= 200)
    description = models.CharField(max_length= 200)
    createDate = models.DateTimeField(auto_now_add=True)
    menuItemId = models.ForeignKey('MenuItem', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name
    

class Supplier(models.Model):
    name = models.CharField(max_length= 200)
    emailAddress = models.EmailField()
    homeAddress = models.CharField(max_length= 200)
    website = models.CharField(max_length= 200)
    phoneNumber = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
