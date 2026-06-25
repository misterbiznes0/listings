from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)

            login(request, user)
            messages.success(request, 'Регистрация прошла успешно.')

            return redirect('/profile/')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
