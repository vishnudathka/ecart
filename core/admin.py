from django.contrib import admin
from core import models

admin.site.register(models.UnitModel)
admin.site.register(models.CategoryModel)
admin.site.register(models.ProductModel)

