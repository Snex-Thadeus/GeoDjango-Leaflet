from django.contrib import admin
from django.contrib.gis import admin #Should come after the first one
from . models import CoffeTypes, Shop, County, Street
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
@admin.register(CoffeTypes)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(LeafletGeoAdmin):
    pass


@admin.register(County)
class CountyAdmin(LeafletGeoAdmin):
    pass


@admin.register(Street)
class StreetAdmin(LeafletGeoAdmin):
    pass
