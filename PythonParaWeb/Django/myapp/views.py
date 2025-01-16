from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    title = 'Welcome  To Django Course'
    return render(request,'index.html', {'title': title})

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)


def about(request):
    return render(request, "about.html")

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def tasks(request):
    #task = get_object_or_404(Task, id = id)

    tastks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tastks})

def create_task(request):
   if request.method == 'GET':
       return render(request, 'create_task.html', {'form': CreateNewTask()})
   else:
       Task.objects.create(title = request.POST['title'], description = request.POST['description'], project_id=2)
       return redirect('tasks')
   
def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {'form': CreateNewProject()})
    else:
         print(request.POST)
         Project.objects.create(name= request.POST['name'])
         redirect('projects')
    