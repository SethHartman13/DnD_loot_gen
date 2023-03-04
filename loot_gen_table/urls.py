from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='loot-gen-tabel-home'),
    path('about', views.about, name="about_me")
]