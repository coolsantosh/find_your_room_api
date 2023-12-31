from django.contrib import admin
from .models import User


class UserModelAdmin(admin.ModelAdmin):
    list_display=["id","name","email","mobile","city","district"]


admin.site.register(User,UserModelAdmin)
