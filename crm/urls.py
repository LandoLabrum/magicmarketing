from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('blueprint/', views.blueprint, name="blueprint"),
    # path('success/', views.success, name="success"),
]