from django.urls import path, include
from .views import home, download, templates

urlpatterns = [
    path('', home, name="home"),
    path('download', download, name="download"),
    path('templates', templates, name="templates"),


]
