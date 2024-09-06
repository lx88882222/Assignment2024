from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),
    path('add_holiday/<int:year>/<int:month>/<int:day>/', views.add_holiday, name='add_holiday'),
    path('remove_holiday/<int:year>/<int:month>/<int:day>/', views.remove_holiday, name='remove_holiday'),
    path('profile/', views.profile_view, name='profile'), 
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]