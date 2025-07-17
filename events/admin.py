from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "start_time", "end_time", "location", "organizer")
    list_filter = ("start_time", "location")
    search_fields = ("title", "description", "location")
    ordering = ("start_time",)
    autocomplete_fields = ("organizer", "attendees")  # Agar ular ForeignKey/ManyToMany bo‘lsa

