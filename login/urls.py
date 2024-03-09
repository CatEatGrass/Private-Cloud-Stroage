# coding = utf-8
# Dragon's Python3.8 code
# Created at 2021/5/10 21:01
# Edit with PyCharm

from django.urls import path

from . import views

urlpatterns = [
    path('user_login/', views.user_login, name='login'),
    path('user_register/',views.user_register,name='register'),
    #, name='login'  ,name='logout'
    path('user_logout/',views.user_logout,name='logout'),
]