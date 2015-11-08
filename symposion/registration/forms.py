from django import forms
from django.utils.translation import ugettext_lazy as _

from markitup.widgets import MarkItUpWidget

from symposion.registration.models import Attendee, Registration
from symposion.registration.utils import validate_3_plus_4

class AttendeeForm(forms.ModelForm):

    captcha = forms.IntegerField(
        label = _(u"How much 3 + 4 makes?"),
        help_text = _(u"Anti-bot"),
        validators=[validate_3_plus_4])

    class Meta:
        model = Attendee
        fields = [
            "email",
            "name",
            "interests",
        ]
        widgets = {
            "interests": MarkItUpWidget(),
        }

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = [
            "prerequistes",
            "max_attendees",
        ]
        widgets = {
            "prerequistes": MarkItUpWidget(),
        }
