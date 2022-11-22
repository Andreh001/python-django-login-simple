from django.urls import path
from . import views


urlpatterns = [
    path('', views.signin, name='Login'),
    path('panel/', views.panel, name='Panel'),
    path('logout', views.signut, name='Logout')
]
