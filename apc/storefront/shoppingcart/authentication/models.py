from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length= 200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length= 300)
    image = models.ImageField(upload_to='MEDIA_URL', blank=True, null=True)
    category = models.ManyToManyField('Category', related_name = 'MenuItem')
    alergies = models.CharField(max_length= 200, blank=True)
 #   orderDetailsId = models.OneToOneField('OrderDetail',on_delete=models.CASCADE,default=None)

    
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
    totalAmount = models.IntegerField()
    orderStatus = models.CharField(max_length=50)
    createDate = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField('MenuItem', related_name='Order', blank=True)
   # orderDetailId = models.ForeignKey('OrderDetail', on_delete=models.CASCADE)
   # customerId = models.ForeignKey('Customer', on_delete=models.CASCADE)
   # deliveryAgentId = models.ForeignKey('DeliveryAgent', on_delete=models.CASCADE)
   # staffId = models.ForeignKey('Staff', on_delete=models.CASCADE)
    paymentStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.orderDate

class Customer(models.Model):
    name = models.CharField(max_length= 200)
    emailaddress = models.EmailField()
    phoneNumber = models.IntegerField()
    homeAddress = models.CharField(max_length= 200)
    city = models.CharField(max_length= 200)
    postcode = models.CharField(max_length= 200)
    createDate = models.DateTimeField(auto_now_add=True)
    userPassword = models.CharField(max_length=50)
    
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
    totalAmount = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)
    orderID = models.ForeignKey('Order', on_delete=models.CASCADE)

    def __str__(self):
        return self.totalAmount
    
class Ingredint(models.Model):
    name = models.CharField(max_length= 200)
    price = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    recipeId = models.ForeignKey('Recipe', on_delete=models.CASCADE, default=None)
    supplierId = models.ForeignKey('Supplier', on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length= 200)
    description = models.CharField(max_length= 200)
    createDate = models.DateTimeField(auto_now_add=True)
    menuItemId = models.ForeignKey('MenuItem', on_delete=models.CASCADE)

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
