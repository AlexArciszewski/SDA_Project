"""
URL configuration for Final_Project_SDA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
#główny urls aplikacji
#tu wrzucamy z widoki z urls

from django.urls import path
from main_web.views import covid_app, new_user, edit_user, delete_user
from .views import dashboard

urlpatterns = [

    path('covid_app/', covid_app, name="covid_app"),    #tu z views z apki wrzucamy http://127.0.0.1:8000/Final_Project_SDA/covid_app/
    path('users/create/', new_user, name='create-user'),
    path('users/edit/<int:id>/', edit_user, name="edit-user"),   #edycja filmow po id stąd <int:id>
    path('users/delete/<int:id>/', delete_user, name="delete-user"),
    path('dashboard/', dashboard, name='dashboard')

]
