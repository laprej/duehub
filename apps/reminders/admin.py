# apps/reminders/admin.py

from django.contrib import admin

from .models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "due_at",
        "exported",
    )

    list_filter = (
        "exported",
    )

    search_fields = (
        "title",
        "notes",
    )
