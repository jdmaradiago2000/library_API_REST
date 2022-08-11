from django.contrib import admin

# Register your models here.
from .models import Shelf, ShelfBookCopy

admin.site.register(Shelf)
admin.site.register(ShelfBookCopy)
