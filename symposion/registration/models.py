from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from markitup.fields import MarkupField

from symposion.schedule.models import Presentation

class Registration(models.Model):
    """A registration object linked to a presentation
    """

    presentation = models.OneToOneField(Presentation, related_name="registration")
    prerequistes = MarkupField(
        help_text = _(u"Softwares to be installed, version, etc."),
        verbose_name = _("Prerequistes"),
        null = True,
        blank = True,)
    max_attendees = models.IntegerField(verbose_name = _("Max attendees"),)

    def __unicode__(self):
        return _(u"Registration to %s") % self.presentation

    def all_attendees(self):
        return self.attendees.all()

    @property
    def attendees_nb(self):
        return self.attendees.count()

    def places_left(self):
        return (self.max_attendees - self.attendees_nb)

    def is_closed(self):
        """True if max attendees number is reached"""
        return self.max_attendees <= self.attendees_nb

class Attendee(models.Model):
    """Attendee to a talk or a presentation
    """

    #~ user = models.OneToOneField(User, null=True, related_name="attendee_profile")
    register_to = models.ForeignKey('Registration', related_name="attendees")
    email = models.EmailField(
        help_text = _(u"Used in case of cancelling"),
        verbose_name = _("Email"),)
    name = models.CharField(max_length = 100, verbose_name = _(u"Your name or pseudo"),)
    interests = models.TextField(
        help_text = _(u"Your project"),
        null=True,
        blank=True,
        verbose_name = _("Interests"),)

    def __unicode__(self):
        return self.name
