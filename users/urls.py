from django.urls import path, include
from users import views
from users.views import signup, custom_login

urlpatterns = [

    path("", include("django.contrib.auth.urls")),
    path("signup", signup, name="signup"),
    path("activate/<uidb64>/<token>", views.activate, name='activate'),
    path("login", custom_login, name="login"),
    path("", views.user_info, name='user_info'),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("reset/<uidb64>/<token>", views.passwordResetConfirm, name='password_reset_confirm'),

]