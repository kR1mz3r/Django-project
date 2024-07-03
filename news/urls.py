from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='news'),
    path('<int:pk>/', ViewNews.as_view(), name="view_news"),
    path('add-news/', CreateNews.as_view(), name="add_news")
]



