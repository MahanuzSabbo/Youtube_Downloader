from django.urls import path
from .import views

urlpatterns = [
    # path('', views.Instaloader),
    # path('', views.download_video),
    path('', views.index)
]