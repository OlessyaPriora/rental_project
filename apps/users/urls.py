from django.urls import path
from apps.users.views.user_views import *


urlpatterns = [
    path('register/', RegisterUserGenericView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', UserListGenericView.as_view()),
    path('details/', UserRetrieveUpdateDestroyGenericView.as_view()),
]