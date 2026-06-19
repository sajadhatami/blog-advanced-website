from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
# Register your models here.




class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('created_at',)


    #user admin detail page
    fieldsets = (
        ("Authentication", {'fields': ('email', 'password')}),
        ("permissions", {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('groups permissions', {'fields': ('groups', 'user_permissions')}),
        ('login date', {'fields': ('last_login',)}),
    )
    #add user detail page
    add_fieldsets = (
        ("Authentication", {'fields': ('email', 'password1', 'password2')}),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)