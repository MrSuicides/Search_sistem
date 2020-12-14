from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.new_info, name='new_info'),
    path('create', views.create, name='create'),
    path('<int:pk>/delete', views.ProductDelete.as_view(), name='product-delete'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product-details')

]