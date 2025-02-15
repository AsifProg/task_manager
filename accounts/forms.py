from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Profile
from .widgets import CustomClearableFileInput


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'profile_picture', 'full_name', 'bio']
        labels = {
            'profile_picture': '',
        }
        widgets = {
            'profile_picture': CustomClearableFileInput(attrs={
                'class': 'w-md text-gray-400 font-semibold text-sm bg-white border '
                        'file:cursor-pointer cursor-pointer file:border-0 file:py-3 file:px-4 '
                        'file:mr-4 file:bg-gray-100 file:hover:bg-gray-200 file:text-gray-500 rounded',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 '
                            'focus:ring-primary-600 focus:border-primary-600 dark:bg-gray-700 dark:border-gray-600 '
                            'dark:text-white',
                'rows': 4,
                'placeholder': 'Write your bio here'
            }),
            'full_name':forms.TextInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
                'placeholder': 'Type your full name',
                'required': True
            })
        }
