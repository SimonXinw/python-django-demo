# tasks/views.py

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# 任务清单
def task_list(request):
    # 从数据库获取Task对象列表
    tasks = Task.objects.all()
    # 指定渲染模板并向模板传递数据
    return render(request, "tasks/task_list.html", {"tasks": tasks})

# 任务创建
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})
