# apps/reminders/views.py

from django.shortcuts import redirect, render

from .forms import ReminderForm
from .models import Reminder


def reminder_list(request):
    """
    Display all reminders ordered by due date.
    """
    reminders = Reminder.objects.order_by("due_at")

    return render(
        request,
        "reminders/reminder_list.html",
        {
            "reminders": reminders,
        },
    )


def reminder_create(request):
    """
    Create a new reminder.
    """

    if request.method == "POST":
        form = ReminderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("reminders:list")

    else:
        form = ReminderForm()

    return render(
        request,
        "reminders/reminder_form.html",
        {
            "form": form,
        },
    )
