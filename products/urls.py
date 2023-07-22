from django.urls import path

from . import views

urlpatterns = [
    path('',views.product_list_view, name='product-list'),
    path('<int:pk>',views.product_detail_view),
    path('product_set/', views.ProductViewSet.as_view(actions=views.ProductViewSet.action_methods), name='product-list'),
]
