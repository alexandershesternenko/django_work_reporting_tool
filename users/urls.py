from django.urls import path, include
from users import views
from users.views import signup


urlpatterns = [

    path("", include("django.contrib.auth.urls")),
    path('signup', signup, name='signup'),
    path("user_info", views.user_info, name='user_info'),
    # path('/add', CreateNoteView.as_view(), name='add_note'),
    # path('<int:pk>/', NoteDetailView.as_view(), name='detail_note'),
    # path('<int:pk>/edit/', EditNoteView.as_view(), name='edit_note'),
    # path('<int:pk>/delete/', DeleteNoteView.as_view(), name='delete_note'),
    # path('', include('django.contrib.auth.urls')),
]