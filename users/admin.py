from django.contrib import admin

# Register your models here.
from .models import UserLibrary

# class AdminUser(UserAdmin):
#     username=None
# class UserAdmin(admin.ModelAdmin):
#     fields =('email','is_library')
admin.site.register(UserLibrary)
