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
    price = models.FloatField()
    description = models.CharField(max_length= 200)
    image = models.ImageField(upload_to='menu_images/')
    
    def _str_(self):
        return self.name