from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_home),
    path('all_prod/',views.get_home),
]