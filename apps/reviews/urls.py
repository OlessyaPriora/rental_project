from django.urls import path
from apps.reviews.views.review_views import ReviewCreateGenericView, ReviewListGenericView

urlpatterns = [
    # Путь для создания отзыва и рейтинга
    path('', ReviewCreateGenericView.as_view(), name='review_create'), # Путь для создания отзыва и рейтинга
    # Путь для просмотра отзыва и рейтинга конкретного объявления
    path('<int:advertisement_id>/', ReviewListGenericView.as_view(), name='reviews_list'),
]
