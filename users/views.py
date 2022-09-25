from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from users.forms.sign_up import SignUpForm
from users.models import CustomUser


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/sing_up.html', {'form': form})


def user_info(request):
    return render(request, 'user_info.html')
