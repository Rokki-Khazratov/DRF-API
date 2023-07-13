from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_home),
    path('all_products/',views.get_home),
]