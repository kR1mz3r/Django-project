from django.urls import path
from .views import *

urlpatterns = [
    path('', UserView.as_view(), name='account'),
    path('upload_avatar/', upload_avatar, name="upload_avatar"),
    path('logout/', user_logout, name="logout")
]



