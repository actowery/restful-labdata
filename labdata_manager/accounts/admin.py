from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Employee


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'payment_method',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('payment_method',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('payment_method',)}),)
 
admin.site.register(CustomUser, CustomUserAdmin)

class EmployeeAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'is_admin',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('is_admin',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('is_admin',)}),)
 
admin.site.register(Employee, EmployeeAdmin)