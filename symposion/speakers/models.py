import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

from markitup.fields import MarkupField


class Speaker(models.Model):

    SESSION_COUNT_CHOICES = [
        (1, "One"),
        (2, "Two")
    ]

    user = models.OneToOneField(User, null=True, related_name="speaker_profile")
    name = models.CharField(
        _("Name"),
        max_length=100,
        help_text=_("As you would like it to appear in the "
                    "conference program.")
    )
    biography = MarkupField(
        _("Biography"),
        blank=True,
        help_text=_("A little bit about you.  Edit using "
                       "<a href='http://warpedvisions.org/projects/"
                       "markdown-cheat-sheet/target='_blank'>"
                       "Markdown</a>.")
    )
    organisation = models.CharField(max_length=100, blank=True)
    city = models.CharField(_('City'),max_length=255, blank=True)
    need_travel = models.BooleanField(_('Need travel?'), default=False)
    travel_information = models.TextField(
        _('Travel information'),
        help_text=_("It's up to us to buy travel tickets in advance, "
            "so tell your constraints, your preference, or even the "
            "travel reference you would like to take"),
        blank=True
    )
    need_hosting = models.BooleanField(_('Need hosting?'), default=False)
    homestay = models.BooleanField(_('Ok for homestay?'), default=False)
    photo = models.ImageField(upload_to="speaker_photos", blank=True)
    annotation = models.TextField(blank=True)  # staff only
    invite_email = models.CharField(max_length=200, unique=True, null=True, db_index=True)
    invite_token = models.CharField(max_length=40, db_index=True)
    created = models.DateTimeField(
        default=datetime.datetime.now,
        editable=False
    )

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        if self.user:
            return self.name
        else:
            return u"?"

    def get_absolute_url(self):
        return reverse("speaker_edit")

    @property
    def email(self):
        if self.user is not None:
            return self.user.email
        else:
            return self.invite_email

    @property
    def all_presentations(self):
        presentations = []
        if self.presentations:
            for p in self.presentations.all():
                presentations.append(p)
            for p in self.copresentations.all():
                presentations.append(p)
        return presentations
