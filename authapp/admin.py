from django.contrib import admin
from .models import User, ProfileVendor, ProfileClient, ImageProfileVendor, ImageProfileBride
from jet.admin import CompactInline


class ProfileVendorInline(CompactInline):
    model = ProfileVendor
    extra = 1


class ProfileClientInline(CompactInline):
    model = ProfileClient
    extra = 1


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_bride', 'phone', 'email')
    inlines = [ProfileVendorInline, ProfileClientInline]


class ProfileVendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_preview_vendor', 'city', 'number_people')


class ProfileClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_preview_client', 'city', 'number_people')


admin.site.register(User, UserModelAdmin)
admin.site.register(ProfileVendor, ProfileVendorAdmin)
admin.site.register(ProfileClient, ProfileClientAdmin)
admin.site.register(ImageProfileVendor)
admin.site.register(ImageProfileBride)
