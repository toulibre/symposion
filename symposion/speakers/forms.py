from django import forms

from markitup.widgets import MarkItUpWidget

from symposion.speakers.models import Speaker


class SpeakerForm(forms.ModelForm):

    class Meta:
        model = Speaker
        fields = [
            "name",
            "biography",
            "organisation",
            "photo",
            "city",
            "need_travel",
            "need_hosting",
        ]
        widgets = {
            "biography": MarkItUpWidget(),
        }
