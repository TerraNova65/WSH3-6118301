from django.urls import path
from .views import attend, attend_summary
from . import views

urlpatterns = [
    path('attend/', attend, name='attend'),
    path('attend_summary/', attend_summary, name='attend-summary'),
    path('', views.homepage, name='homepage'),
]
