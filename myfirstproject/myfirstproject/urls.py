"""
URL configuration for myfirstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myfirstproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('aboutus/', views.aboutus, name="aboutus"),
    path('submitform/', views.submitform, name="submitform"),
    path('', views.homepage,name="home"),
    path('courses/', views.course),
    path('calculater/', views.calculater),
    path('even_odd/', views.even_odd),
    path('marksheet/', views.marksheet),
    path('courses/<str:courseid>', views.coursedetail),
    path('userform/', views.userform, name="userform"),
    path('newsdetail/<slug>', views.news_detail),
    path('servicedetail/', views.service_detail,name="servicedata"),
    path('contact/', views.contact, name="contact"),
    path('savecontact/', views.save_contact, name="save_contact"),
]
