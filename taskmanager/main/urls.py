from django.urls import path
from . import views
urlpatterns = [
#    path('', views)
#path('', views.index)
    path('', views.index),
    path('about', views.about),
]