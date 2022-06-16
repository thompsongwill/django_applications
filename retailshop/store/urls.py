
from django.urls import path
from . import views





urlpatterns = [ 
              path('', views.index, name='home'),
              path('product/<str:product_id>', views.details, name='details'),
              path('addproduct/', views.add_product, name='add_product'),
              ]


