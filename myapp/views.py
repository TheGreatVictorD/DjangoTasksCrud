# Create your views here.
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject


def index(request):
    title = 'Django course¡¡ '
    return render(request, 'index.html', {'title': title})


def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)


def about(request):
    return render(request, 'about.html')


def projects(request):
    projects = Project.objects.all()
    project_bool = True
    if not projects:
        project_bool = False
    return render(request, 'projects/project.html',
                  {'projects': projects, 'project_bool': project_bool})


def create_project(request):
    success_message = ''
    if request.method == 'POST':
        form = CreateNewProject(request.POST)  # Los datos del formulario se pasan aquí
        if form.is_valid():  # se verifica que los datos del formulario sean validos
            #  Como los datos son validos se crea una instancia en la tabla 'Project' con los datos del formulario
            Project.objects.create(
                # Se obtienen los datos del formulario con el método cleaned_data y se pasan como parametros
                name=form.cleaned_data['name']
            )
            success_message = 'Project successfully created!'
            print(success_message)
            form = CreateNewProject()  # Resetea el formulario después de guardar
            return redirect('projects')
    else:
        form = CreateNewProject()
        return render(request, 'projects/create_project.html', {'form_project': form, 'success_message': success_message})


def delete_project(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        project.delete()
        return redirect('projects')  # Redirige a la lista de proyectos después de eliminar
    return render(request, 'projects/project.html')  # O redirige a un lugar adecuado


def project_detail(request, project_id):
    project_detail = get_object_or_404(Project, id=project_id)
    print(project_detail)
    tasks_project = Task.objects.filter(project_id=project_id)
    return render(request, 'projects/detail.html', {
        'project_detail': project_detail,
        'tasks_project': tasks_project})


def task(request):
    tasks = Task.objects.all()
    task_bool = False
    if not tasks:
        task_bool = True
    return render(request, 'tasks/task.html', {'tasks': tasks, 'task_bool': task_bool})


def create_task(request):
    success_message = ''
    if request.method == 'POST':
        form = CreateNewTask(request.POST)  # Los datos del formulario se pasan aquí
        if form.is_valid():  # se verifica que los datos del formulario sean validos
            #  Como los datos son validos se crea una instancia en la tabla 'Project' con los datos del formulario
            Task.objects.create(
                # Se obtienen los datos del formulario con el método cleaned_data y se pasan como parametros
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                project=form.cleaned_data['project']
            )
            success_message = 'Task successfully created!'
            print(success_message)
            form = CreateNewTask()  # Resetea el formulario después de guardar
    else:
        # Show form interface
        form = CreateNewTask()
    return render(request, 'tasks/create_task.html', {'form': form, 'success_message': success_message})


def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('tasks')
    return render(request, 'tasks/task.html')


def toggle_task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done
    task.save()
    return redirect('tasks')
