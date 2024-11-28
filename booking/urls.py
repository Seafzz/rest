from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('create/', views.create_reservation, name='create_reservation'),
]
