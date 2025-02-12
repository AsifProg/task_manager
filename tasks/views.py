from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import TaskForm, ProjectForm


@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})


@login_required
def project_list(request):
    """View all projects."""
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def project_detail(request, project_id):
    """View details of a specific project."""
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})


@login_required
def task_list(request, project_id=None):
    """View all tasks or filter by project."""
    if project_id:
        project = get_object_or_404(Project, id=project_id)
        tasks = Task.objects.filter(project=project)
    else:
        project = None
        tasks = Task.objects.all()

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'project': project})


@login_required
def task_detail(request, task_id):
    """View details of a specific task."""
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_create(request):
    """Allows users to create a task by selecting a project from a dropdown."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_list', project_name=task.project.name)
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, task_id):
    """Delete a specific task."""
    task = get_object_or_404(Task, id=task_id)
    project_id = task.project.id
    task.delete()
    return redirect('task_list_by_project', project_id=project_id)

@login_required
def project_delete(request, project_id):
    """Delete a specific project and all its tasks."""
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('project_list')

