from django.db import models
from django.urls import reverse
# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    image=models.ImageField(upload_to='department',blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def get_url(self):
        return reverse('storeapp:products_by_department', args=[self.slug])

    def __str__(self):
        return  '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('storeapp:prodetail',args=[self.department.slug,self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)


