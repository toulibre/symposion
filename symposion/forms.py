try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = None

import account.forms
from django import forms
from django.utils.translation import ugettext_lazy as _


class SignupForm(account.forms.SignupForm):

    first_name = forms.CharField(label=_("First name"))
    last_name = forms.CharField(label=_("Last name"), required=False)
    email_confirm = forms.EmailField(label=_("Confirm Email"))

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        field_order = [
            "first_name",
            "last_name",
            "email",
            "email_confirm",
            "password",
            "password_confirm"
        ]
        del self.fields["username"]
        if not OrderedDict or hasattr(self.fields, "keyOrder"):
            self.fields.keyOrder = field_order
        else:
            self.fields = OrderedDict((k, self.fields[k]) for k in field_order)

    def clean_email_confirm(self):
        email = self.cleaned_data.get("email")
        email_confirm = self.cleaned_data["email_confirm"]
        if email:
            if email != email_confirm:
                raise forms.ValidationError(
                    "Email address must match previously typed email address")
        return email_confirm
