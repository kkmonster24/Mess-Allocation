from django.urls import path
from . import views

app_name = 'messapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.reg, name='reg'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('feedback/', views.feedback, name='feedback'),
    path('profile/', views.profile, name='profile'),
    path('select_dates/', views.select_dates, name='select_dates'),
    
    path('dumb/', views.showCalender, name='showCalender'),
]