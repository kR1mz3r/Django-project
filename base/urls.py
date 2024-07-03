from django.urls import path
from .views import *

urlpatterns = [
    path('', BaseList.as_view(), name='base'),
    path('<int:pk>/', BaseProjectView.as_view(), name="base_detail"),
]





