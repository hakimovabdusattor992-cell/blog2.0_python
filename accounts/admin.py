from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserForm, CustomUserChange
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserForm
    form = CustomUserChange
    model = CustomUser
    
    # Ro'yxatda nimalar ko'rinishi
    list_display = [ 'username', 'first_name', 'last_name', 'email', 'age','is_staff']

    # Tahrirlash sahifasida age ko'rinishi uchun
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )

    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'password', 'password_confirm', 'email', 'age'),
    }),
)

admin.site.register(CustomUser, CustomUserAdmin)