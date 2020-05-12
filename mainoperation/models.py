from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Category(models.Model):
    category_name= models.CharField(max_length=50)
    Create_on=models.DateField(auto_now=True)
    description= models.CharField(max_length=500)
    image= models.FileField(max_length=100,null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        """Unicode representation of Viewpoint."""
        return self.category_name

    

class Product(models.Model):
    name= models.CharField(max_length=50)
    description= models.TextField(max_length=500)
    image= models.FileField(max_length=100,null=True,blank=True)
    Create_on=models.DateField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        """Unicode representation of Viewpoint."""
        return self.name


class Promotion(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=500)
    image= models.FileField(max_length=100,null=True,blank=True)
    discount=models.CharField(max_length=100)
    Create_on=models.DateField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    
