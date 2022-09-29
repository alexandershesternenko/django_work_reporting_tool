from django.urls import path, include
from users import views
from users.views import signup, change_password

urlpatterns = [

    path("", include("django.contrib.auth.urls")),
    path("signup", signup, name="signup"),
    path("", views.user_info, name='user_info'),
    path("change_password", change_password, name='change_password'),
]