"""EmployeeManagemnt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from Task import views
from EmployeeManagemnt import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^load/', views.WelcomeView.as_view()),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^home/', views.HomePageView.as_view()),
    url(r'^logout/', views.LogoutView.as_view()),
    url(r'^update/(?P<item_id>[-\d]+)', views.UpdateView.as_view()),
    url(r'^update_data/', views.UpdateDataView.as_view()),
    url(r'^delete/(?P<item_id>[-\d]+)', views.DeleteView.as_view()),
    url(r'^addinv/', views.AddInv.as_view()),
    url(r'^add_inv_data/', views.AddInvView.as_view()),
    
]
