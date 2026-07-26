# apps/reminders/models.py

from django.db import models


class Reminder(models.Model):
    """
    A reminder waiting to be exported to Due.
    """

    title = models.CharField(max_length=200, help_text="Short description shown in Due.")

    notes = models.TextField(blank=True)

    due_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    exported = models.BooleanField(default=False)

    def __str__(self):
        return self.title
