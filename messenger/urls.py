from django.urls import path
from .views import *

urlpatterns = [
    path('', MessengerView.as_view(), name='messenger'),
    path('messenger/load_messages/<int:user_id>/', load_messages, name='load_messages'),
]



