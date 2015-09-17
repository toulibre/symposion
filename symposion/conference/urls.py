from django.conf.urls import patterns, url


urlpatterns = patterns(
    "symposion.conference.views",
    url(r"^users/$", "user_list", name="user_list"),
    url(r"^speakers/$", "speaker_list", name="speaker_list"),
)
