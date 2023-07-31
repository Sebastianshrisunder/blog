from django.urls import path
from . import views
urlpatterns = [
    path('',views.basic,name='basic'),
    path('index',views.index,name='index'),
    path('post/<str:pk>', views.post,name='post'),
    path('create',views.create,name='create'),
    path('delete/<str:pk>', views.delete,name='delete'),
    path('update/<str:pk>', views.update,name='update'),
    path('register', views.register, name='register'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('home', views.home, name='home'),
    path('view', views.see, name='charts')
]
