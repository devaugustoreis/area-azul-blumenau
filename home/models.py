from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    zip_code = models.CharField(max_length=8)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=6)
    complement = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, null=True, blank=True)
    credits = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Vehicles(models.Model):
    VEHICLES_TYPE = (
        ('C', 'Car'),
        ('M', 'Moto'),
        ('O', 'Other'),
    )
    license_plate = models.CharField(max_length=7)
    entry_time = models.DateTimeField(null=True ,blank=True)
    timer = models.IntegerField(null=True, blank=True)
    vehicle_type = models.CharField(max_length=1, choices=VEHICLES_TYPE)
    client = models.ManyToManyField(Client)

    def __str__(self):
        return self.name
