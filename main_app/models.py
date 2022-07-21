from unicodedata import name
from django.db import models
from django.urls import reverse
# Create your models here.
POWER = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low')
)

class Shop(models.Model):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('shop_detail', kwargs={'pk': self.id})

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    shop = models.ManyToManyField(Shop)

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})    

class Mods(models.Model):
  mod = models.CharField(max_length=100)
  power = models.CharField(
    max_length=1,
    choices=POWER,
    default=POWER[0][0]
  )
  
  car = models.ForeignKey(Car, on_delete=models.CASCADE)
  def __str__(self):
     return f"{self.get_power_display()} on {self.mod}"