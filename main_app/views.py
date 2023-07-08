from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView

from django.views.generic import DetailView

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Project :
    def __init__(self, title, description, start_date, end_date, importance, created_at,   updated_at ):
        self.title = title
        self.idescription = description
        self.start_date = start_date
        self.end_date = end_date
        self.importance = importance
        self.created_at = created_at
        self.updated_at = updated_at

projects = [
    Project(
        "Productivity Tracker",
        "Develop a productivity tracking application that helps users monitor and optimize their daily tasks. The app will include features such as task management, time tracking, goal setting, and performance analytics.",
        "2022-01-01",
        "2022-02-01",
        "high",
        "2022-01-01 00:00:00",
        "2022-01-01 00:00:00"
    ),
    Project(
        "E-commerce Website Redesign",
        "Redesign an existing e-commerce website to enhance the user experience, improve the visual aesthetics, and optimize the overall performance. The redesign will involve updating the UI/UX, implementing responsive design, and integrating new payment gateways.",
        "2022-02-01",
        "2022-03-01",
        "medium",
        "2022-02-01 00:00:00",
        "2022-02-01 00:00:00"
    ),
    Project(
    "Website Content Migration",
    "Migrate website content from an old platform to a new CMS...",
    "2022-03-15",
    "2022-04-15",
    "high",
    "2022-03-01 00:00:00",
    "2022-03-01 00:00:00"
),
Project(
    "Social Media Marketing Campaign",
    "Plan and execute a social media marketing campaign...",
    "2022-05-01",
    "2022-06-30",
    "medium",
    "2022-05-01 00:00:00",
    "2022-05-01 00:00:00"
),
Project(
    "Mobile App UI/UX Design",
    "Design user interfaces and experiences for a mobile application...",
    "2022-07-01",
    "2022-08-15",
    "low",
    "2022-07-01 00:00:00",
    "2022-07-01 00:00:00"
),
Project(
    "Data Migration and Integration",
    "Migrate and integrate data from multiple sources into a unified system...",
    "2022-09-01",
    "2022-10-31",
    "high",
    "2022-09-01 00:00:00",
    "2022-09-01 00:00:00"
),
]

class ProjectList(TemplateView):
    template_name = "project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = projects
        return context
    

    
class ProjectDetail(DetailView):
    model = Project
    template_name = "project_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = kwargs['project_id']
        # Retrieve the project object based on the project_id
        # Add the project object to the context
        return context
