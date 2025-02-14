from django import forms
from .models import Task, Project
from django.contrib.auth import get_user_model


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = get_user_model().objects.all()
        self.fields['project'].queryset = Project.objects.all()

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            'placeholder': 'Type task name',
            'required': True
        })
    )

    priority = forms.ChoiceField(
        choices=Task._meta.get_field('priority').choices,
        widget=forms.Select(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white'
        })
    )

    status = forms.ChoiceField(
        choices=Task._meta.get_field('status').choices,
        widget=forms.Select(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white'
        })
    )

    assigned_to = forms.ModelChoiceField(
        queryset=get_user_model().objects.none(),
        empty_label="Select User",
        widget=forms.Select(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white'
        })
    )

    project = forms.ModelChoiceField(
        queryset=Project.objects.none(),
        empty_label="Select Project",
        widget=forms.Select(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white'
        })
    )

    due_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            'required': True
        })
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-600 focus:border-primary-600 dark:bg-gray-700 dark:border-gray-600 dark:text-white',
            'rows': 4,
            'placeholder': 'Write task description here'
        }),
        required=False
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date',
                  'priority', 'status', 'assigned_to', 'project']
