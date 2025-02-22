from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data("username")
            password = form.cleaned_data("password")
            user = authenticate(request, username, password)
            if user is not None:
                login(request, user)
                return redirect("review-list")
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
        context = {
            "form": form,
        }
        return render(request,
                      "users/auth.html",
                      context)
