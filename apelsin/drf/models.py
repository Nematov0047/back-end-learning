from django.db import models

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

class Contact(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField('phone number', max_length=40)

    def __str__(self):
        return self.name + ' | ' + self.contact