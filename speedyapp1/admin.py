from django.contrib import admin
from .models import *
from accounts.models import *


class BrandAdmin(admin.ModelAdmin):
    list_display=['brand_name']

class BrandmodelsAdmin(admin.ModelAdmin):
    list_display=['model_name']


# Register your models here.
admin.site.register(profile)
admin.site.register(Brand)
admin.site.register(Brand_models)
admin.site.register(Spares)
admin.site.register(Cart)
admin.site.register(CartItem)
