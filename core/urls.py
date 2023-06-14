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
#główny urls

from django.contrib import admin
from django.urls import path, include
#from main_web.views import test_response to poszło do url apki

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),    #"""http://127.0.0.1:8000/admin/"""  w path"admin/" to to samo co ten link z lewej
 #   path('test/', test_response)                      #tu z views z apki wrzucamy
    path('', include('main_web.urls')), #http://127.0.0.1:8000/Final_Project_SDA/test/
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   #tu media url i media root gdzie przechowujemy zdjecia
