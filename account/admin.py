from django.contrib import admin
from account import models

admin.site.register(models.LocationModel)
admin.site.register(models.AddressModel)
admin.site.register(models.ProfileModel)
