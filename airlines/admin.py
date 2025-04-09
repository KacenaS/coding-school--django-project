from django.contrib import admin
from airlines.models import Airline, Alliance, Airport

# 1. the easiest connection of models
# admin.site.register(Airline)
# admin.site.register(Alliance)

# 2. changing the view - more columns showing more information
@admin.register(Alliance)
class AllianceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'airline_name','airline_code')


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('id', 'airport_name', 'airport_code')


