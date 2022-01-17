from django.urls import path

from .views import projects, project, createProject, updtaeProject


urlpatterns = [
    path('', projects, name="projects"),
    path('project/<str:pk>/', project, name="project"),

    path('create-project/', createProject, name="create-project"),
    path('updtae-project/<str:pk>/', updtaeProject, name="updtae-project")
]
