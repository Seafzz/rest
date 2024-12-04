from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('edit/<int:pk>/', views.edit_reservation, name='edit_reservation'),
    path('delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
    path('profile/', views.update_profile, name='profile'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
]

