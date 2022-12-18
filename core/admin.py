from django.contrib import admin
from .models import TripPlace, Activity


# Register your models here.

class ActivityInline(admin.TabularInline):
    model = Activity


class TripPlaceAdmin(admin.ModelAdmin):
    inlines = [ActivityInline]


admin.site.register(TripPlace, TripPlaceAdmin)


