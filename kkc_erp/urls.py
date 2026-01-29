from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views  # Built-in views
from core.views import dashboard, custom_logout
from workflows.views import submit_leave

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    
    # Explicit login (fixes 404 on /accounts/login/)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # Custom logout (your view to fix 405)
    path('accounts/logout/', custom_logout, name='logout'),
    
    # Optional: Add password reset if needed (built-in)
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # Leave form
    path('submit-leave/', submit_leave, name='submit_leave'),
]