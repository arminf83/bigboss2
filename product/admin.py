from django.contrib import admin
from .models import Product , Comment , Category

@admin.register(Product)
 
class Productadmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
 
class Comentadmin(admin.ModelAdmin):
    pass
@admin.register(Category)
 
class Categoryadmin(admin.ModelAdmin):
    pass