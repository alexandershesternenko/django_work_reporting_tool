from django.urls import path, include
from users import views
from users.views import signup, change_password
from django.contrib.auth import views as auth_views


urlpatterns = [

    path("", include("django.contrib.auth.urls")),
    path("signup", signup, name="signup"),
    path("", views.user_info, name='user_info'),
]