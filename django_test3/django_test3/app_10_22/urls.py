from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('project_create/', views. Create_project.as_view(), name='pr'),
    path('registration/', views. Registration.as_view()),
    path('project/<int:id>/', views.project),
    path('edit project/<int:id>/', views.edit_project)
#path('test/', views. TestPage.as_view())
]
