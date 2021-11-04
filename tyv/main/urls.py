from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('guest', views.guest, name='guest'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
]