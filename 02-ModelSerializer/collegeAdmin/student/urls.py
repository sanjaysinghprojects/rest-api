from . import views
from django.urls import path

urlpatterns = [
    path('getstudent/', views.studentlist),
    path('getstudent/<pk>/', views.studentdetail),]
