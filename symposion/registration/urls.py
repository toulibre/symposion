from django.conf.urls import patterns, url


urlpatterns = patterns("symposion.registration.views",
    url(r"^presentation/(?:(?P<pk>\d+)/)?$", "register_to_presentation", name="register_to_presentation"),
    url(r"^presentation/(?:(?P<pk>\d+)/)?add/$", "registration_add", name="registration_add"),
    url(r"^presentation/(?:(?P<pk>\d+)/)?edit/$", "registration_edit", name="registration_edit"),
)
