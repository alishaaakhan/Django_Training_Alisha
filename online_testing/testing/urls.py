from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signup-success/', views.signup_success, name='signup_success'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('test/<int:test_id>/', views.start_test, name='start_test'),
    path('test-history/', views.test_history, name='test_history'),
    path('logout/', views.logout, name='logout'),
]
