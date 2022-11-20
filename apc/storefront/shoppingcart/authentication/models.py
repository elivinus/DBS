from django.db import models

# Create your models here.

class ItemList(models.Model):
    name = models.CharField(max_length= 200)
    
    def _str_(self):
        return self.name
    
    
class Item(models.Model):
    itemList = models.ForeignKey(ItemList, on_delete=models.CASCADE)
    itemName = models.CharField(max_length = 300)
    complete = models.BooleanField()
    
    def _str_(self):
         return self.itemName

class MenuItem(models.Model):
    name = models.CharField(max_length= 200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.CharField(max_length= 300)
    image = models.ImageField(upload_to='menu_images/')
    category = models.CharField(max_length= 200, blank=True)
    alergies = models.CharField(max_length= 200, blank=True)
    
        
    def _str_(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length= 200)
    emailaddress = models.EmailField(max_length= 200)
    phoneNumber = models.IntegerField()
    homeAddress = models.CharField(max_length= 200)
    city = models.CharField(max_length= 200)
    postcode = models.CharField(max_length= 200)
    createDate = models.DateTimeField(auto_now_add=True)
    userPassword = models.CharField(max_length=50)
    
    def _str_(self):
        return self.name
    
class DeliveryAgent(models.Model):
    name = models.CharField(max_length= 200)
    emailAddress = models.EmailField(max_length= 200)
    phoneNumber = models.IntegerField()
    homeAddress = models.CharField(max_length= 200)
    city = models.CharField(max_length= 200)
    postcode = models.CharField(max_length= 200)
    createDate = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.name
    
class Staff(models.Model):
    name = models.CharField(max_length= 200)
    emailAddress = models.EmailField(max_length= 200)
    phoneNumber = models.IntegerField()
    homeAddress = models.CharField(max_length= 200)
    city = models.CharField(max_length= 200)
    postcode = models.CharField(max_length= 200)
    createDate = models.DateTimeField(auto_now_add=True)
    userPassword = models.CharField(max_length=50)
    
    def _str_(self):
        return self.name
    
class Order(models.Model):
    orderDate = models.DateTimeField(auto_now_add=True)
    totalAmount = models.IntegerField()
    orderStatus = models.CharField(max_length=50)
    createDate = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.orderDate

class OrderDetails(models.Model):
    totalAmount = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.totalAmount
    
class Ingredints(models.Model):
    name = models.CharField(max_length= 200)
    price = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
    
class Recipes(models.Model):
    name = models.CharField(max_length= 200)
    description = models.CharField(max_length= 200)
    createDate = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
    

class Supplier(models.Model):
    name = models.CharField(max_length= 200)
    emailAddress = models.CharField(max_length= 200)
    homeAddress = models.CharField(max_length= 200)
    website = models.CharField(max_length= 200)
    phoneNumber = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
