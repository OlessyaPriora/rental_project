from django.urls import path
from apps.reviews.views.review_views import ReviewCreateGenericView, ReviewListGenericView

urlpatterns = [
    path('', ReviewCreateGenericView.as_view(), name='review_create'),
    path('<int:advertisement_id>/', ReviewListGenericView.as_view(), name='reviews_list'),
]
