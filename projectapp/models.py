from django.db import models


class CATEGORY_PRODUCTS (models.Model):
    code = models.CharField(primary_key=True, max_length=5)
    description = models.TextField(max_length=500)


class PRODUCTS (models.Model):
    productId = models.CharField(primary_key=True, max_length=5)
    categoryCode = models.ForeignKey(CATEGORY_PRODUCTS, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    quantityAvailable = models.IntegerField()
    Cost = models.DecimalField(max_digits=10, decimal_places=2)
    sellingPrice = models.DecimalField(max_digits=10, decimal_places=2)


class CUSTOMERS (models.Model):
    customerId = models.CharField(primary_key=True, max_length=5)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    email = models.EmailField()
    homePhone = models.CharField(max_length=13)
    cellPhone = models.CharField(max_length=13)


class ORDERS (models.Model):
    orderNumber = models.IntegerField(primary_key=True)
    customerid = models.ForeignKey(CUSTOMERS, on_delete=models.CASCADE)
    orderDate = models.DateField()
    shippedDate = models.DateField()
    paymentDate = models.DateField()


class ORDER_DETAIL (models.Model):
    orderNumber = models.ForeignKey(ORDERS, on_delete=models.CASCADE)
    productId = models.ForeignKey(PRODUCTS, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = (('orderNumber', 'productId'),)


class Person(models.Model):
    name = models.CharField(max_length=255)
