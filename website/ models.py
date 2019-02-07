from django.contrib.auth.models import User
from django.db import models


# Product Model

class Product(models.Model):
'''This Model defines all the relationships and attributes of the Products table in our
    database.

    Author: Group

    Methods:
        __str__ -- title
'''
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    productType = models.ForeignKey(ProductType, on_delete= models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    deletedOn = models.DateField(default = None)

    def __str__(self):
        ''' returns a string representation of the model '''
        return self.title

# Customer Model

class Customer(models.Model):
'''This Model defines all of the relationships and attributes of the Customer table.

    Author: Group

    Methods:
        __str__ -- user
'''
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.CharField(max_length= 200)
    phoneNumber = models.CharField(max_length= 12)
    deletedOn = models.DateField(default = None)

    def __str__(self)
        ''' returns a string representation of the model '''
        return self.user

# Payment Type Model

class PaymentType(models.Model):
'''Defines a model for the relationships and attributes for the Payment Table.

    Author: Group

    Methods:
        __str__ -- name
'''
    name = models.CharField(max_length= 50)
    accountNumber = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete= models.PROTECT)
    deletedOn = models.DateField(default = None)

    def __str__(self):
        ''' returns a string representation of the model '''
        return self.name

# Order Model

class Order(models.Model):
'''Defines a model for a customer order and includes customers payment info

    Author: Group

    Methods:
        __str__ -- id
'''

    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)
    paymentType = models.ForeignKey(PaymentType, on_delete = models.PROTECT)
    isCompleted = models.BooleanField(default = False)
    product = models.ManyToManyField(Product, blank=True, through='ProductOrder')
    deletedOn = models.DateField(default = None)

    def __str__(self):
        ''' returns a string representation of the model '''
        return self.id

# Product Order

class ProductOrder(models.Model):
''' Defines a model for the connection between Product and Order models

    Author: Group

    Methods:
        __str__ -- order, product
'''

    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    deletedOn = models.DateField(default = None)

    def __str__(self):
        ''' returns a string representation of the model '''
        return self.order, self.product

# Product Type

class ProductType(models.Model):
'''Defines a model for the relationships and attributes of the ProductType table

    Author: Group

    Methods:
        __str__ -- name
'''
    name = models.CharField(max_length = 100)
    deletedOn = models.DateField(default = None)

    def __str__(self):
        ''' returns a string representation of the model '''
        return self.name