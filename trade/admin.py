from django.contrib import admin

from .models import OneshirtUser, Item, Trade

# Register your models here.
admin.site.register(OneshirtUser)
admin.site.register(Item)
admin.site.register(Trade)
