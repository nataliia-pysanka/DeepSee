from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('api/products/', views.ProductsListView.as_view(), name='products'),
    path('api/create/', views.CreateProductView.as_view(), name='create'),
    path('api/store/', views.OrderProductView.as_view(), name='store'),
    # path('api/products/int<pk>', views.GetProductInfoView.as_view()),
]
