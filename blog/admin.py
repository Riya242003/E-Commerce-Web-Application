from django.contrib import admin

# Register your models here.
from .models import Blogpost
# model register here
admin.site.register(Blogpost)