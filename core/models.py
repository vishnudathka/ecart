from django.db import models
from django.urls import reverse
from django.conf import settings
USER = settings.AUTH_USER_MODEL



class ImageModel(models.Model):
    name = models.CharField(max_length=255)
    path = models.ImageField(upload_to="image/")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    class Meta:
        abstract =True

    def __str__(self):
        return  self.name   


class ProductImageModel(ImageModel):
    path =models.ImageField(upload_to="product/image/", default="default/product.jpg")



class UnitModel(models.Model):
    name = models.CharField(max_length=128)
    base = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
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
    images = models.ManyToManyField(ProductImageModel)   
    unit = models.ForeignKey(UnitModel, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse("core:product_details",args=(self.id)) 



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