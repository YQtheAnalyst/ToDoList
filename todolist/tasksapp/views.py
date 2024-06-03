from django.shortcuts import render

from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):

    tasks = task.objects.all()
    form = TaskForm()

    context = {'tasks': tasks, 'forms': form}

    return render(request, 'tasksapp/list.html', context)
