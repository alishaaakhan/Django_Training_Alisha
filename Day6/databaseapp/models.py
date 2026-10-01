from django.db import models

# Create your models here.
class Client(models.Model):
    clientID = models.IntegerField()
    clientName = models.CharField(max_length = 30)
    clientCompany = models.CharField(max_length = 30)

    def __str__(self):
        return self.clientName
    
class Customer(models.Model):
    customerID = models.IntegerField()
    customerName = models.CharField(max_length = 30)
    customerPhone = models.IntegerField()
 
    def __str__(self):
        return self.customerName

class Order(models.Model):
    orderID = models.IntegerField()
    orderName = models.CharField(max_length = 30)
    oderPrice = models.FloatField()

    def __str__(self):
        return self.orderName  