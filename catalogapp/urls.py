from django.urls import path

from catalogapp.views import PlaceListView, PlaceDetailView, AreaListView, AreaDetailView, ImagePlaceListView, \
    ImagePlaceDetailView, ImageAreaListView, ImageAreaDetailView, ImageTerritoryListView, ImageTerritoryDetailView, \
    ImageOutsiteRegListView, ImageOutsiteRegDetailView, ImageWeddingListView, ImageWeddingDetailView, \
    ImageWelcomeZoneListView, ImageWelcomeZoneDetailView, OutsiteRegistrationListView, OutsiteRegistrationDetailView, \
    WelcomeZoneListView, WelcomeZoneDetailView


app_name = 'catalog'

urlpatterns = [
    # Площадки
    path('places/', PlaceListView.as_view(), name='place-list'),
    path('place/<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),

    # Места
    path('areas/', AreaListView.as_view(), name='area-list'),
    path('area/<int:pk>/', AreaDetailView.as_view(), name='area-detail'),

    # Картинки площадок
    path('image-places/', ImagePlaceListView.as_view(), name='image-place-list'),
    path('image-place/<int:pk>/', ImagePlaceDetailView.as_view(), name='image-place-detail'),

    # Картинки мест
    path('image-area/', ImageAreaListView.as_view(), name='image-area-list'),
    path('image-area/<int:pk>/', ImageAreaDetailView.as_view(), name='image-areas-detail'),

    # Картинки территорий
    path('image-territory/', ImageTerritoryListView.as_view(), name='image-territory-list'),
    path('image-territory/<int:pk>/', ImageTerritoryDetailView.as_view(), name='image-territory-detail'),

    # Картинки выездных регистраций
    path('image-outsite-reg/', ImageOutsiteRegListView.as_view(), name='image-outsite-reg-list'),
    path('image-outsite-reg/<int:pk>/', ImageOutsiteRegDetailView.as_view(), name='image-outsite-reg-detail'),

    # Картинки прошедших свадеб
    path('image-wedding/', ImageWeddingListView.as_view(), name='image-wedding-list'),
    path('image-wedding/<int:pk>/', ImageWeddingDetailView.as_view(), name='image-wedding-detail'),
    # WelcomeZone
    path('welcome-zones/', WelcomeZoneListView.as_view(), name='welcome-zone-list'),
    path('welcome-zone/<int:pk>/', WelcomeZoneDetailView.as_view(), name='welcome-zone-detail'),
    # Картинки прошедших свадеб
    path('image-welcome-zone/', ImageWelcomeZoneListView.as_view(), name='image-welcome-zone-list'),
    path('image-welcome-zone/<int:pk>/', ImageWelcomeZoneDetailView.as_view(), name='image-welcome-zone-detail'),

    # Выездные регистрации
    path('outsite_registration/', OutsiteRegistrationListView.as_view(), name='outsite-registration-list'),
    path('outsite_registration/<int:pk>/', OutsiteRegistrationDetailView.as_view(), name='outsite-registration-detail')
]