# from django.conf.urls import url
from django.urls import path
from visitors import views

urlpatterns = [ 
    path('visitors/', views.visitor_list),
    path('visitors/<int:pk>', views.visitor_detail)
]
