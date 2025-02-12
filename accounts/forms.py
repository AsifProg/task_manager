from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'profile_picture']
