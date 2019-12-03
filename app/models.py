from django.db import models

class Category(models.Model):
    code = models.CharField(max_length=30,unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=100, verbose_name='Tên')
    description = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.name        
