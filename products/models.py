from django.db import models

# Create your models here.


class Category(models.Model):

    """This Meta Class specifies model plural name. 
    Needed to correct issue in Django admin that assumes 
    plural of a model only requires addition of s."""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    placeholder_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True,)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Basket(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    placeholder_img = models.ImageField(null=True, blank=True)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2)
    basket = models.ForeignKey(
        'Product', related_name='basket', null=True, blank=True, on_delete=models.SET_NULL)
    cheese1 = models.ForeignKey(
        'Product', related_name='cheese1', null=True, blank=True, on_delete=models.SET_NULL)
    cheese2 = models.ForeignKey(
        'Product', related_name='cheese2', null=True, blank=True, on_delete=models.SET_NULL)
    cheese3 = models.ForeignKey(
        'Product', related_name='cheese3', null=True, blank=True, on_delete=models.SET_NULL)
    meat1 = models.ForeignKey(
        'Product', related_name='meat1', null=True, blank=True, on_delete=models.SET_NULL)
    meat2 = models.ForeignKey(
        'Product', related_name='meat2', null=True, blank=True, on_delete=models.SET_NULL)
    drink = models.ForeignKey(
        'Product', related_name='drink', null=True, blank=True, on_delete=models.SET_NULL)
    
    
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
