from django.urls import path

from apps.users.views.user_views import UserListGenericView, RegisterUserGenericView

urlpatterns = [
    path('register/', RegisterUserGenericView.as_view()),
    path('users/', UserListGenericView.as_view()),
    ]