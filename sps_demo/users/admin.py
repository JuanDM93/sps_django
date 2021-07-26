from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
from users.models import User

@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = [
        'username', 'email',
    ]