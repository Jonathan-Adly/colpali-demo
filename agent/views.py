from django.conf import settings
from django.shortcuts import render


def home(request):
    if settings.LOCAL:
        base_url = f"ws://{request.get_host()}"
    else:
        base_url = f"wss://{request.get_host()}"
    return render(request, "home.html", {"base_url": base_url})
