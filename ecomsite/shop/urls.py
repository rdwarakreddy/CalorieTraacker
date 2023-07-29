from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('Out_of_stock/', views.Out_of_stock, name='Out_of_stock'),
    path('<int:id>',views.detail,name = 'detail'),
    path('checkout',views.checkout,name ='checkout'),


    # Other URL patterns for the 'shop' app
]
