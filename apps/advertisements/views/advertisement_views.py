from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from apps.advertisements.models import Advertisement
from apps.advertisements.permission import IsLandlordOrReadOnly, IsAuthorOrReadOnly
from apps.advertisements.serializers.advertisement_serializer import AdvertisementSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Вьюшка для просмотра и создания объявления
class AdvertisementListCreateGenericView(ListCreateAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [IsLandlordOrReadOnly] # Разрешение только для арендодателя
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
# словарь, где ключи - это имена полей модели, а значения - это списки операторов фильтрации,
# которые могут быть применены к соответствующим полям.
    filterset_fields = {
        'price': ['gte', 'lte'],
        'city': ['icontains'],# пользователь может указать часть названия города,
        # и результаты запроса будут отфильтрованы по соответствию этому критерию.
        'rooms': ['gte', 'lte'],
        'housing_type': ['exact'],# пользователь может указать конкретный тип жилья,
        # и результаты запроса будут отфильтрованы по точному соответствию этому критерию.
}
    search_fields = ['title', 'description'] #писок полей, которые будут использованы для поиска
    ordering_fields = ['price', 'created_at'] #список полей, которые могут быть исп-ны для сорт-и результатов запроса

#функция автоматического присвоения авторства к создаваемому объекту
    def perform_create(self, serializer):
        serializer.save(author=self.request.user) # при создании объекта будет автоматически установлен автор,
        # связанный с текущим пользователем

#метод в котором будут возвращены только активные объявления
    def get_queryset(self):
        return Advertisement.objects.filter(is_active=True)


#для обновления и удаления объявления только автор может иметь доступ
class AdvertisementRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [IsAuthorOrReadOnly]












