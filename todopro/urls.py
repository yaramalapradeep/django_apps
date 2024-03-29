"""todopro URL Configuration

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
from django.urls import path
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('login/',views.loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('signup',views.signup_view,name='signup'),
    path('tlist/',views.list_view,name='tlist'),
    path('dlist/',views.done_view,name='dlist'),
    path('addlist/',views.add_view,name='addlist'),
    path('update/<int:id>/',views.update_view,name='update'),
    path('delete/<int:id>/',views.delete_view,name='delete'),
]
