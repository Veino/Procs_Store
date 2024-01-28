from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ProcsUserCreationForm, ProcsUserChangeForm
from .models import ProcsUser


class ProcsUserAdmin(UserAdmin):
    add_form = ProcsUserCreationForm
    form = ProcsUserChangeForm
    model = ProcsUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "image",
                "phone_number", "birthday", "isProcsAdmin",
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(ProcsUser, ProcsUserAdmin)