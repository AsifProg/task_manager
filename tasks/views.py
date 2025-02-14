from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .forms import TaskForm, ProjectForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if not form.is_valid():
            return JsonResponse({"success": False, "error": form.errors.as_text()}, status=400)

        form.save()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)


@login_required
def project_detail(request, project_id):
    """View details of a specific project."""
    project = get_object_or_404(Project, id=project_id)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            "id": project.id,
            "name": project.name,
            "description": project.description
        })

    return render(request, 'projects/project_list.html', {'project': project})


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
    User = get_user_model()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if not form.is_valid():
            return JsonResponse({"success": False, "error": form.errors.as_text()}, status=400)

        form.save()

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"success": True})

        return redirect("task_list")

    form = TaskForm()
    form.fields['assigned_to'].queryset = User.objects.all()

    return render(request, "tasks/task_form.html", {"form": form})



@login_required
def task_delete(request, task_id):
    """Delete a specific task."""
    task = get_object_or_404(Task, id=task_id)
    project_id = task.project.id
    task.delete()
    return redirect('task_list_by_project', project_id=project_id)


@csrf_exempt
def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        project.delete()
        return JsonResponse({"success": True})

    return JsonResponse({"success": False}, status=400)
