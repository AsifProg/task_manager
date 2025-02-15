from django.shortcuts import render, redirect
from django.contrib.auth import login
from allauth.socialaccount.models import SocialAccount # type: ignore
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import RegisterForm, ProfileUpdateForm


def register(request):
    if request.user.is_authenticated:
        return redirect('task_list')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('task_list')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    is_oauth_user = SocialAccount.objects.filter(user=user).exists()

    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'accounts/profile.html', {'form': form, 'is_oauth_user': is_oauth_user})

