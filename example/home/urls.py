from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # user browser
    path('themesindex', views.themesIndex, name='themesindex'),
    path('themesabout', views.themesAbout, name='themesabout'),
    path("home/", views.home, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]
