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
    email = models.EmailField(max_length= 200)
    phone = models.IntegerField()
    address = models.CharField(max_length= 200)
    city = models.CharField(max_length= 200)
    Postcode = models.CharField(max_length= 200)
    create_date = models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return self.name

