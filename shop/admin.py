from django.contrib import admin

# Register your models here.
# admin login -> Riya and password -> 1234

from .models import Product,Contact,Orders,OrderUpdate
# model register here
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)