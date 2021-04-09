from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage, Category, ProductAlternative, ParoductAccessories


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductAlternative)
admin.site.register(ParoductAccessories)