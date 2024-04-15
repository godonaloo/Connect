from django.urls import path
from .views import LoginView, DashboardView, RegisterView, PasswordResetView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/',DashboardView.as_view(), name='dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
]
