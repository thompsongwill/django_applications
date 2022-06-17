from django.contrib import admin
from .models import Product

# Register your models here.


admin.site.site_header = "Retail Store Admin"
admin.site.index_title = "Retail Admin Dashboard"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('seller','title','price','image')
    search_fields = ('title',)
    
    def set_price_to_zeero(self,request,queryset):
        queryset.update(price=0)
        
    actions = ('set_price_to_zero',)
    
    # list_editable = ('title','price')
    





admin.site.register(Product,ProductAdmin)