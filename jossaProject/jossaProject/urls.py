"""jossaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('institute/',views.institute_chart,name='institute'),
    path('rank/',views.rank,name='rank'),
    path('get_data/', views.get_data, name='get_data'),
    path('get_institute_data/', views.get_institute_data, name='get_institute_data'),
    path('institute_rank/',views.institute_rank,name= 'institute_rank'),
    path('get_program_data/', views.get_program_data, name='get_program_data'),
    path('program/',views.program,name= 'academic_program'),
    path('get_popular_institute/',views.get_popular_institute,name='get_popular_institute'),
    path('popular_institute/',views.popular_institute,name='popular_institute'),
    path('get_popular_course/',views.get_popular_course,name='get_popular_course'),
    path('popular_course/',views.popular_course,name='popular_course'),
    path('degree/',views.degree,name='degree'),
    path('get_degree/',views.get_degree,name='get_degree'),
    path('quota/',views.quota,name='quota'),
    path('get_quota/',views.get_quota,name='get_quota'),
]
