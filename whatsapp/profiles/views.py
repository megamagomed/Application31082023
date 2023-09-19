from django.shortcuts import render, redirect
from .models import ProfileModel, MessageModel
from .forms import RegistrationForm, LoginForm, ProfileForm, MessagesForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def start_page(request):
    content = request.user
    all_users = User.objects.all()
    return render(
        request,
        "profiles/start_page.html",
        {"content": content, "all_users": all_users},
    )


def registration_page(request):
    content = RegistrationForm(request.POST or None)
    if content.is_valid():
        username = content.cleaned_data["username"]
        email = content.cleaned_data["email"]
        password = content.cleaned_data["password"]
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        ProfileModel.objects.create(user=user)
        return redirect("/login/")

    return render(request, "profiles/registration.html", {"registration_data": content})


def login_page(request):
    content = LoginForm(request.POST or None)
    if content.is_valid():
        username = content.cleaned_data["username"]
        password = content.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, "profiles/login_page.html", {"login_data": content})


def logout_view(request):
    logout(request)
    return redirect("/")


def profile_view(request):
    print("adsfasdfdasf")
    content = ProfileModel.objects.get(user=request.user)
    profile_form = ProfileForm(request.POST or None)
    if profile_form.is_valid():
        name = profile_form.cleaned_data["name"]
        about_yourself = profile_form.cleaned_data["about_yourself"]
        content.name = name
        content.about_yourself = about_yourself
        content.save()
        return redirect("/profile")

    return render(
        request,
        "profiles/profile_page.html",
        {"profile_form": profile_form},
    )


def messages_view(request, pk):
    message_form = MessagesForm(request.POST or None)
    if request.POST:
        if message_form.is_valid():
            message_text = message_form.cleaned_data["message_text"]
            user = User.objects.get(id=pk)
            chat = MessageModel.objects.create(
                message=message_text, sender=request.user, receiver=user
            )
        return redirect(f"/messages/{pk}")
    user = User.objects.get(id=pk)
    chat1 = MessageModel.objects.filter(sender=request.user, receiver=user)
    chat2 = MessageModel.objects.filter(sender=user, receiver=request.user)

    return render(
        request,
        "profiles/message_page.html",
        {"message_form": message_form, "chat": reversed(chat1.union(chat2))},
    )
