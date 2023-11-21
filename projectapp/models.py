from django.db import models


class CategoryProduct(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255)

    def __str__(self):
        return 'Código: ' + self.code + ' | ' + 'Descripción: ' + self.description


class Product(models.Model):
    productId = models.CharField(primary_key=True, max_length=5)
    categoryCode = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    quantityAvailable = models.IntegerField()
    Cost = models.DecimalField(max_digits=10, decimal_places=2)
    sellingPrice = models.DecimalField(max_digits=10, decimal_places=2)


class Customer(models.Model):
    customerId = models.CharField(primary_key=True, max_length=255)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    dateOfBirth = models.DateField()
    email = models.EmailField()
    homePhone = models.CharField(max_length=50)
    cellPhone = models.CharField(max_length=50)

    def __str__(self):
        return ('Nombre: ' + self.firstName + ' ' + self.lastName + ' | '
                + 'Número identificación: ' + self.customerId)


class Order(models.Model):
    orderNumber = models.IntegerField(primary_key=True)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    orderDate = models.DateField()
    shippedDate = models.DateField()
    paymentDate = models.DateField()


class OrderDetail (models.Model):
    orderNumber = models.ForeignKey(Order, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = (('orderNumber', 'productId'),)
