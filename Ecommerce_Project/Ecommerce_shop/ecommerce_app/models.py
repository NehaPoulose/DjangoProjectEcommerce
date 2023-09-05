from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 250,unique = True)
    slug = models.SlugField(max_length = 250,unique = True)
    image = models.ImageField(upload_to = 'category',blank = True)
    category_description = models.TextField(blank = True)

    class Meta:
        ordering = ['name',]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('ecommerce_app:Product Collection',args=[self.slug])


    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='product', blank=True)
    product_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits = 10,decimal_places = 2)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    stock = models.IntegerField()
    available = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


    class Meta:
        ordering = ['name']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('ecommerce_app:Productdetails',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)