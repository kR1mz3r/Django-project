from django.urls import path
from .views import *

urlpatterns = [
    path('', ProjectTaskList.as_view(), name='project'),
    path('<int:pk>/', ViewProject.as_view(), name="view_task"),
    path('<int:pk>/update_files/', update_files, name="update_files"),
]



