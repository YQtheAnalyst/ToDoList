from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):

    tasks = task.objects.all()
    form = TaskForm()

    # create item, let it save whatever you have inputted and submitted, and redirect to base page
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'forms': form}

    return render(request, 'tasksapp/list.html', context)


def updateTask(request, pk):
    tasks = task.objects.get(id=pk)

    form = TaskForm(instance=tasks) # ?

    if request.method == "POST":
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'forms':form}

    return render(request, 'tasksapp/update_task.html', context)

# Make queries once the model is built:
# https://docs.djangoproject.com/en/5.0/topics/db/queries/