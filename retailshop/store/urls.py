
from django.urls import path
from . import views
app_name = 'store'





urlpatterns = [ 
              path('', views.index, name='home'),
              path('product/<str:product_id>', views.details, name='details'),
              path('products/add/', views.add_product, name='add_product'),
              path('products/update/<int:id>/', views.update_product, name='update'),
              path('products/delete/<int:id>/', views.delete, name='delete'),
              path('products/mylistings', views.listings, name='listings'),
              ]


