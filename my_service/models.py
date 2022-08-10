from django.db import models


class VehicleModel(models.Model):
    brand = models.CharField(max_length=50, null=False, blank=False)
    model = models.CharField(max_length=50, null=False, blank=False)


class Service(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)


class Vehicle(models.Model):
    registration_number = models.CharField(max_length=10, unique=True, null=False, blank=False)
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, null=False, blank=False)
    vin_code = models.CharField(max_length=20, null=False, blank=False)
    client = models.CharField(max_length=50, null=False, blank=False)


class Order(models.Model):
    date = models.CharField(max_length=20, null=False, blank=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False, blank=False)
    total = models.IntegerField(null=False, blank=False)
    is_done = models.BooleanField(default=False)


class OrderDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=False, blank=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
