from django.shortcuts import render
from .models import ProfileModel


def start_page(request):
    content = request.user
    print(content)
    return render(request, "profiles/start_page.html", {"content": content})

def registration_page(request):
