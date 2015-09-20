from django.http import Http404
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from symposion.speakers.models import Speaker


@login_required
def user_list(request):

    if not request.user.is_staff:
        raise Http404()

    return render(request, "conference/user_list.html", {
        "users": User.objects.all(),
    })

@login_required
def speaker_list(request):

    if not request.user.is_staff:
        raise Http404()

    speakers = Speaker.objects.all()

    return render(request, "conference/speaker_list.html", {
        "speakers": speakers,
    })
