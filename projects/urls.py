from django.urls import path

from .views.project_view import ProjectView


urlpatterns = [
    path('project/', ProjectView.as_view()),
]
