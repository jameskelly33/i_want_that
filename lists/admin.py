from django.contrib import admin
from .models import WishListItem




class WishListItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'url',
        'price',
        'person',
        
        
    )


admin.site.register(WishListItem, WishListItemAdmin)
