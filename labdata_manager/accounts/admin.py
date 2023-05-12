from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Employee


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
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
    list_display = [
        'email',
        'username',
        'is_supervisor',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('is_supervisor',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('is_supervisor',)}),)
 
admin.site.register(Employee, EmployeeAdmin)