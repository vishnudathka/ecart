from django.db import models


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
