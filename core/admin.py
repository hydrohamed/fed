from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import FloodEvent


@admin.register(FloodEvent)
class FloodEventAdmin(LeafletGeoAdmin):
    list_display = ('id', 'location')
