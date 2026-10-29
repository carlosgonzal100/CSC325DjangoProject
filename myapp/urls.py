from myapp import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/hello/', views.hello_api, name='hello_api'),
]