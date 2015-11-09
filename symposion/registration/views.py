from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _

from symposion.registration.forms import AttendeeForm, RegistrationForm
from symposion.schedule.models import Presentation


def register_to_presentation(request, pk):
    """Form to register"""

    presentation = get_object_or_404(Presentation, pk=pk)

    if request.method == "POST":
        form = AttendeeForm(request.POST)
        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.register_to = presentation.registration
            attendee.save()
            messages.success(request, _("You registered successfully."))
            return redirect("schedule_presentation_detail", presentation.pk)

    else:
        form = AttendeeForm()

    return render(request, "registration/register_to.html", {
        "form": form,
        "presentation": presentation,
    })

@login_required
def registration_add(request, pk):
    """Form to add registration form to a presentation"""

    presentation = get_object_or_404(Presentation, pk=pk)

    if not request.user.is_staff:
        if request.user.speaker_profile not in [s for s in presentation.speakers()]:
            raise Http404()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.presentation = presentation
            registration.save()
            messages.success(request, _("Registration form has been created successfully."))

    else:
        form = RegistrationForm()

    return render(request, "registration/registration_edit.html", {
        "form": form,
        "presentation": presentation,
    })

@login_required
def registration_edit(request, pk):
    """Form to edit registration form for a presentation"""

    presentation = get_object_or_404(Presentation, pk=pk)
    registration = presentation.registration

    if not request.user.is_staff:
        if request.user.speaker_profile not in [s for s in presentation.speakers()]:
            raise Http404()

    if request.method == "POST":
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            messages.success(request, _("Registration form has been updated successfully."))

    else:
        form = RegistrationForm(instance=registration)

    return render(request, "registration/registration_edit.html", {
        "form": form,
        "presentation": presentation,
    })
