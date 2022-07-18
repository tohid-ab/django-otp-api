from django.contrib import admin
from .models import PhoneNumberUser, OTPRequest
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class PhoneNumberAdmin(UserAdmin):
    list_display = ('username', 'id', 'first_name', 'last_name', 'is_staff')


class OTPAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'receiver', 'created',)


admin.site.register(OTPRequest, OTPAdmin)
admin.site.register(PhoneNumberUser, PhoneNumberAdmin)
