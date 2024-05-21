from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import CustomUser


# Define a form for the user model
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username',)  # Include other fields as needed


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username',)  # Include other fields as needed


# Define the admin class
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'is_active')
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'access_level')}),
        # Removed date_joined from here as well
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active')
        }
        ),
    )

    # readonly_fields = (
    #     (None, {
    #     'readonly_fields' : ()
    # }),
    # )

    readonly_fields = ('joined_at',)
    search_fields = ('username',)
    ordering = ('username',)

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


# Register your models here
admin.site.register(CustomUser, CustomUserAdmin)
# ----------------------
