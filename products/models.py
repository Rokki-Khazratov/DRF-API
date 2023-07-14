from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=355)
    content = models.TextField()
    price = models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
    category_id = models.ForeignKey('Category',on_delete= models.CASCADE,blank=True,null=True)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def __str__(self):
        return self.title
    