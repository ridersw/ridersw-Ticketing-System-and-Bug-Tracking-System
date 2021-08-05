"""TicketTool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from projects.views import project_homepage
from mainapp.views import homepage
from tickets.views import view_tickets, assignedToMyGroup, assignedToMe, submittedByMe, showTickets
from engineer.views import checkUserCreds, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', project_homepage),
    path('', homepage),
    path('tickets/', view_tickets, name="view_tickets"),
    path('assignedToMyGroup/', assignedToMyGroup, name="assignedToMyGroup"),
    path('assignedToMe/', assignedToMe, name="assignedToMe"),
    path('submittedByMe/', submittedByMe, name="submittedByMe"),
    path('showTickets/', showTickets, name="showTickets"),
    path('checkUserCreds/', checkUserCreds),     
    path('logout_view/', logout_view, name="logout_view"),     
]
