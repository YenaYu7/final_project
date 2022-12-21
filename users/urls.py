from django.urls import path
from . import views
app_name= 'users'
urlpatterns =[
    path('login/', views.userslogin, name='login'),
    path('logout/', views.userslogout, name='logout'),
    path('signup/', views.signup, name='signup'),
    ]

