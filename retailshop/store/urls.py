
from django.urls import path
from . import views
app_name = 'store'





urlpatterns = [ 
         
              path('', views.ProductListView.as_view(), name='home'),
             
              path('product/<str:pk>', views.ProductDetailView.as_view(), name='details'),
              path('products/add/', views.AddProductView.as_view(), name='add_product'),
              path('products/update/<int:pk>/', views.UpdateProductView.as_view(), name='update'),
              path('products/delete/<int:pk>/', views.DeleteProductView.as_view(), name='delete'),
              path('products/mylistings', views.listings, name='listings'),
              ]


