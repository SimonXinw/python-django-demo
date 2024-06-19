from django.urls import path
from . import views

# namespace
app_name = "tasks"

urlpatterns = [
    # Retrieve task list
    path("", views.task_list, name="task_list"),
    # Create new task
    path("create/", views.task_create, name="task_create"),
]
