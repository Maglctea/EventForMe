from django.contrib import admin
from .models import Place, Area, ImageArea, ImagePlace, Event, Kitchen, Location, TypeArea, TypePlace, \
    Features, TypeTerritory, WelcomeZone, OutsiteRegistration, ImageTerritory, ImageOutsiteReg, ImageWelcomeZone, \
    ImageTerritory


class ImageTerritoryInline(admin.TabularInline):
    model = ImageTerritory
    extra = 1


class PlaceModelAdmin(admin.ModelAdmin):
    filter_horizontal = ('location', 'kitchen', 'event', 'type_territory', 'type_place')
    list_display = [field.name for field in Place._meta.fields]
    inlines = [ImageTerritoryInline]


class ImageWelcomeZoneInline(admin.TabularInline):
    model = ImageWelcomeZone
    extra = 1


class WelcomeZoneModelAdmin(admin.ModelAdmin):
    inlines = [ImageWelcomeZoneInline]
    list_display = [field.name for field in WelcomeZone._meta.fields]


class TypeTerritoryModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TypeTerritory._meta.fields]


class ImageTerritoryModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ImageTerritory._meta.fields]


class ImageOutsiteRegInline(admin.TabularInline):
    model = ImageOutsiteReg
    extra = 1


class OutsiteRegistrationModelAdmin(admin.ModelAdmin):
    inlines = [ImageOutsiteRegInline]
    list_display = [field.name for field in OutsiteRegistration._meta.fields]


admin.site.register(Place, PlaceModelAdmin)
admin.site.register(Area)
admin.site.register(ImageArea)
admin.site.register(ImagePlace)
admin.site.register(Event)
admin.site.register(Kitchen)
admin.site.register(Location)
admin.site.register(TypeArea)
admin.site.register(TypePlace)
admin.site.register(Features)
admin.site.register(TypeTerritory, TypeTerritoryModelAdmin)
admin.site.register(WelcomeZone, WelcomeZoneModelAdmin)
admin.site.register(OutsiteRegistration, OutsiteRegistrationModelAdmin)
admin.site.register(ImageTerritory, ImageTerritoryModelAdmin)
admin.site.register(ImageOutsiteReg)
