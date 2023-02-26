from django.shortcuts import render, HttpResponse
from home import models
# Create your views here.
def home(request):
    context = {'success' : False, 'name':'Donnie'}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = models.Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success' : True}

    return render(request, 'index.html', context)

def tasks(request):
    allTasks = models.Task.objects.all()
  # print(allTasks)
  # for item in allTasks:
  #     print(item.taskDesc)
    context = {'tasks' : allTasks}
    return render(request, 'tasks.html', context)