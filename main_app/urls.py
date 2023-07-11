from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name='about'),
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projects/new/', views.ProjectCreate.as_view(), name="project_create"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('projects/<int:pk>/update', views.ProjectUpdate.as_view(), name="project_update"),
    path('projects/<int:pk>/delete',views.ProjectDelete.as_view(), name="project_delete"),
]
