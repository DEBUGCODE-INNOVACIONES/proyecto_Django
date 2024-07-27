from django.contrib import admin
from django.urls import path
from DebugCode import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('searchingServices/', views.searchingServices, name='searchingServices'),
    path('search/', views.search, name='search'),
]
