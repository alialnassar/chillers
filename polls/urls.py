from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:chiller_id>/',views.chiller_detials,name='chiller_detials'),
    path('login',views.login,name='login'),
    path('add_chiller',views.add_chiller,name='add_chiller')
]