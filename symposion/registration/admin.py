from django.contrib import admin

from symposion.registration.models import Attendee, Registration


admin.site.register(
    Attendee,
    list_display=("name", "email")
)

admin.site.register(Registration)
