from django.db import models
from django.conf import settings
USER = settings.AUTH_USER_MODEL


class UnitModel(models.Model):
    name = models.CharField(max_length=128)
    baise = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    symbol = models.CharField(max_length=3)
    conversion_rate = models.FloatField(default=1.0)

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=500)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    discription = models.TextField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to="product/image/", default="default/product.jpg")
    unit = models.ForeignKey(UnitModel, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class StockModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.FloatField()
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product)


class CartModel(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    is_checked_out = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class CartItemModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    quantiti = models.FloatField()
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product)