from django.shortcuts import render, redirect
from django.contrib.auth import login
from allauth.socialaccount.models import SocialAccount # type: ignore
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileUpdateForm


def register(request):
    """Handles both manual registration and OAuth login."""
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
    """Handles profile updates."""
    user = request.user
    is_oauth_user = SocialAccount.objects.filter(
        user=user).exists()

    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=user.profile)

    return render(request, 'accounts/profile.html', {'form': form, 'is_oauth_user': is_oauth_user})
