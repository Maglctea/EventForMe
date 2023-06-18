from rest_framework.serializers import ModelSerializer

from authapp.serializers import UserModelSerializer
from catalogapp.models import Place, Area, ImageArea, ImagePlace, TypeArea, Location, Kitchen, Event, TypePlace, \
    Features, TypeTerritory, WelcomeZone, OutsiteRegistration, ImageTerritory, ImageOutsiteReg, ImageWelcomeZone, \
    ImageWedding
from rest_framework import serializers


class ImageTerritorySerializer(ModelSerializer):
    """Сериализатор для картинок территорий"""

    # image = serializers.ImageField(required=False)
    # todo
    class Meta:
        model = ImageTerritory
        fields = "__all__"


class ImageListTerritorySerializer(ModelSerializer):
    """Сериализатор для картинок территорий"""

    class Meta:
        model = ImageTerritory
        fields = "__all__"


class ImageOutsiteRegSerializer(ModelSerializer):
    """Сериализатор для картинок выездной регистрации"""

    class Meta:
        model = ImageOutsiteReg
        fields = '__all__'


class TypePlaceSerializer(ModelSerializer):
    """Сериализатор для типов площадок"""

    class Meta:
        model = TypePlace
        fields = '__all__'


class FeaturesSerializer(ModelSerializer):
    """Сериализатор для особенностей площадки"""

    class Meta:
        model = Features
        fields = '__all__'


class TypeTerritorySerializer(ModelSerializer):
    """Сериализатор для территорий"""

    class Meta:
        model = TypeTerritory
        fields = '__all__'


class ImageWelcomeZoneSerializer(ModelSerializer):
    class Meta:
        model = ImageWelcomeZone
        fields = '__all__'


class WelcomeZoneSerializer(ModelSerializer):
    images_welcome = ImageWelcomeZoneSerializer(many=True)

    class Meta:
        model = WelcomeZone
        fields = '__all__'


class WelcomeZoneCreateSerializer(ModelSerializer):
    """Сериализатор Welcome-Зоны"""

    # images_welcome = ImageWelcomeZoneSerializer(many=True)

    class Meta:
        model = WelcomeZone
        fields = '__all__'


class WelcomeZoneListSerializer(ModelSerializer):
    class Meta:
        model = WelcomeZone
        fields = ('id', 'welcome_desc', 'place')


class OutsiteRegistrationListSerializer(ModelSerializer):
    class Meta:
        model = OutsiteRegistration
        fields = '__all__'


class OutsiteRegistrationSerializer(ModelSerializer):
    """Сериализатор выездной регистрации"""
    images_out_reg = ImageOutsiteRegSerializer(many=True)

    class Meta:
        model = OutsiteRegistration
        fields = '__all__'


class TypeAreaSerializer(ModelSerializer):
    """Сериализатор категории мест внутри площадок для проведения мероприятий"""

    class Meta:
        model = TypeArea
        fields = '__all__'


class EventSerializer(ModelSerializer):
    """Сериализатор ивентов"""

    class Meta:
        model = Event
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    """Сериализатор локаций внутри площадок"""

    class Meta:
        model = Location
        fields = '__all__'


class KitchenSerializer(ModelSerializer):
    """Сериализатор кухни"""

    class Meta:
        model = Kitchen
        fields = '__all__'


class ImageAreaSerializer(ModelSerializer):
    """Сериализатор изображений для мест на площадке"""

    class Meta:
        model = ImageArea
        fields = '__all__'


class ImagePlaceSerializer(ModelSerializer):
    """Сериализатор изображений для мест на площадке"""

    class Meta:
        model = ImagePlace
        fields = '__all__'


class AreaCreateSerializer(ModelSerializer):
    """Сериализатор создания площадки для проведения мероприятий"""
    place_id = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all(), source='place', write_only=True)

    class Meta:
        model = Area
        fields = ('place_id', 'title', 'cover_area', 'type_area', 'min_capacity', 'max_capacity', 'color_hall',
                  'separate_entrance', 'min_price_banquet', 'min_price_rent', 'deposit', 'scheme_of_payment',
                  'detail_location', 'reserved_days')


class AreaListSerializer(ModelSerializer):
    """Сериализатор списка мест внутри площадок для проведения мероприятий"""
    type_area = TypeAreaSerializer()

    class Meta:
        model = Area
        fields = (
        'id', 'type_area', 'min_capacity', 'max_capacity', 'min_price_banquet', 'min_price_rent', 'scheme_of_payment')


class AreaDetailSerializer(ModelSerializer):
    """Сериализатор места внутри площадки для проведения мероприятий"""
    type_area = TypeAreaSerializer()
    images_area = ImageAreaSerializer(many=True)

    class Meta:
        model = Area
        fields = '__all__'


class PlaceCreateSerializer(ModelSerializer):
    """Сериализатор создания площадки для проведения мероприятий"""

    class Meta:
        model = Place
        exclude = ('user',)


class PlaceListSerializer(ModelSerializer):
    """Сериализатор списка площадок для проведения мероприятий"""
    images_place = ImagePlaceSerializer(many=True)
    areas = AreaListSerializer(many=True)

    class Meta:
        model = Place
        fields = ('id', 'title', 'areas', 'images_place', 'cover_place')


class ImageWeddingSerializer(ModelSerializer):
    class Meta:
        model = ImageWedding
        fields = '__all__'


class PlaceDetailSerializer(ModelSerializer):
    """Сериализатор площадки для проведения мероприятий"""
    user = UserModelSerializer()
    images_place = ImagePlaceSerializer(many=True)
    location = LocationSerializer(many=True)
    areas = AreaDetailSerializer(many=True)
    kitchen = KitchenSerializer(many=True)
    event = EventSerializer(many=True)
    type_territory = TypeTerritory()
    type_place = TypePlaceSerializer(many=True)
    type_feature = FeaturesSerializer(many=True)
    images_wedding = ImageWeddingSerializer(many=True)
    welcome_zones = WelcomeZoneSerializer(many=True)
    outsites_reg = OutsiteRegistrationSerializer(many=True)

    class Meta:
        model = Place
        fields = '__all__'
