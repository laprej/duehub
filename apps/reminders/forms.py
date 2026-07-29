# apps/reminders/forms.py

from django import forms

from .models import Reminder


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = [
            "title",
            "notes",
            "due_at",
        ]

        widgets = {
            "due_at": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }
