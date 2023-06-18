from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from catalogapp.permissions import VendorPermission, VendorCanCreatePermission, BrideReadonlyPermission, \
    AdminCanCreatePermission, ReadOnly
from catalogapp.filters import PlaceFilter
from catalogapp.models import Place, Area, ImagePlace, ImageArea, ImageWelcomeZone, ImageWedding, ImageOutsiteReg, \
    ImageTerritory, WelcomeZone, \
    OutsiteRegistration
from catalogapp.serializers import PlaceListSerializer, PlaceDetailSerializer, AreaDetailSerializer, AreaListSerializer, \
    PlaceCreateSerializer, AreaCreateSerializer, ImagePlaceSerializer, ImageAreaSerializer, ImageWelcomeZoneSerializer, \
    ImageWeddingSerializer, ImageOutsiteRegSerializer, ImageTerritorySerializer, WelcomeZoneSerializer, \
    WelcomeZoneListSerializer, WelcomeZoneCreateSerializer, ImageListTerritorySerializer, \
    OutsiteRegistrationSerializer, ImageWeddingSerializer, ImageOutsiteRegSerializer, ImageTerritorySerializer, \
    OutsiteRegistrationListSerializer
from catalogapp.file_upload import FileLoad
from authapp.models import User


class StandarPagination(PageNumberPagination):
    """Стандартная пагинация с 10 полями на 1 странице"""
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 8


class PlaceListView(ListAPIView, CreateAPIView):
    img_array = 'place_img'
    """Представление списка площадок для проведения мероприятий"""
    serializer_class = PlaceListSerializer
    queryset = Place.objects.all()
    filterset_class = PlaceFilter
    pagination_class = StandarPagination
    ordering_fields = ['average_check']

    # permission_classes = [
    #     IsAuthenticatedOrReadOnly | VendorCanCreatePermission | AdminCanCreatePermission | BrideReadonlyPermission]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PlaceListSerializer
        elif self.request.method == 'POST':
            return PlaceCreateSerializer

    def post(self, request, *args, **kwargs):
        if request.data.get(self.img_array):
            if request.user:
                request.data['user'] = request.user.pk
            else:
                request.data['user'] = User.objects.get(pk=1)
            serializer = PlaceCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_create(serializer)
                place = serializer.instance
                place.user = request.user
                place_id = place.id
                # Создаем экземпляр класса FileLoad и вызываем метод, для сохранения картинок площадок с FilePond
                file_load_instance = FileLoad()
                file_load_instance.move_upload_img_for_place(request, self.img_array, place_id)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(f'Bad Request{self.img_array}.required field does not exist', status.HTTP_400_BAD_REQUEST)


class PlaceDetailView(RetrieveAPIView, DestroyAPIView):
    """Представление площадки для проведения мероприятий"""
    serializer_class = PlaceDetailSerializer
    queryset = Place.objects.all()
    filterset_class = PlaceFilter
    permission_classes = [ReadOnly | VendorPermission | BrideReadonlyPermission | IsAdminUser]


class AreaListView(ListAPIView, CreateAPIView):
    img_array = 'area_img'
    """Представление списка площадок для проведения мероприятий"""
    serializer_class = AreaListSerializer
    queryset = Area.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission | IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AreaListSerializer
        elif self.request.method == 'POST':
            return AreaCreateSerializer

    def post(self, request, *args, **kwargs):
        if request.data.get(self.img_array):
            serializer = AreaCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            area = serializer.instance
            area_id = area.id
            file_load_instance = FileLoad()
            file_load_instance.move_upload_img_for_area(request, self.img_array, area_id)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(f'Bad Request {self.img_array}, required field does not exist', status.HTTP_400_BAD_REQUEST)


class AreaDetailView(RetrieveAPIView, DestroyAPIView):
    """Представление площадки для проведения мероприятий"""
    serializer_class = AreaDetailSerializer
    queryset = Area.objects.all()
    # filterset_class = AreaFilter
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorPermission]


class ImagePlaceListView(ListAPIView, CreateAPIView):
    """Представление списка картинок площадки"""
    serializer_class = ImagePlaceSerializer
    queryset = ImagePlace.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]


class ImagePlaceDetailView(RetrieveAPIView, DestroyAPIView):
    """Представление определенной картинки площадки"""
    serializer_class = ImagePlaceSerializer
    queryset = ImagePlace.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | VendorPermission | IsAdminUser, BrideReadonlyPermission]


class ImageAreaListView(ListAPIView, CreateAPIView):
    """Представление списка картинок места"""
    serializer_class = ImageAreaSerializer
    queryset = ImageArea.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]


class ImageAreaDetailView(RetrieveAPIView, DestroyAPIView):
    """Представление определенной картинки места"""
    serializer_class = ImageAreaSerializer
    queryset = ImageArea.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | VendorPermission | IsAdminUser, BrideReadonlyPermission]


class ImageWelcomeZoneListView(ListAPIView, CreateAPIView):
    """Представление списка картинок велком зоны"""
    serializer_class = ImageWelcomeZoneSerializer
    queryset = ImageWelcomeZone.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]


class WelcomeZoneListView(ListAPIView, CreateAPIView):
    img_array = 'welcome_zone_img'
    serializer_class = WelcomeZoneListSerializer
    queryset = WelcomeZone.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data.get(self.img_array):
            serializer = WelcomeZoneCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            zone = serializer.instance
            zone_id = zone.id
            file_load_instance = FileLoad()
            file_load_instance.move_upload_img_for_welcome_zone(request, self.img_array, zone_id)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(f'Bad Request {self.img_array}, required field does not exist', status.HTTP_400_BAD_REQUEST)


class WelcomeZoneDetailView(RetrieveAPIView, DestroyAPIView):
    serializer_class = WelcomeZoneSerializer
    queryset = WelcomeZone.objects.all()


class ImageWelcomeZoneDetailView(RetrieveAPIView, DestroyAPIView):
    """Представление определенной картинки велком зоны"""
    serializer_class = ImageWelcomeZoneSerializer
    queryset = ImageWelcomeZone.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]


class ImageWeddingListView(ListAPIView, CreateAPIView):
    """Представление списка картинок площадки"""
    serializer_class = ImageWeddingSerializer
    queryset = ImageWedding.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]


class ImageWeddingDetailView(RetrieveAPIView, DestroyAPIView):
    """Представление определенной картинки прошлой свадьбы"""
    serializer_class = ImageWeddingSerializer
    queryset = ImageWedding.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]


class ImageOutsiteRegListView(ListAPIView, CreateAPIView):
    """Представление списка картинок выездной регистрации"""
    serializer_class = ImageOutsiteRegSerializer
    queryset = ImageOutsiteReg.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]


class ImageOutsiteRegDetailView(RetrieveAPIView, DestroyAPIView):
    """Представление картинок определенной выездной регистрации"""
    serializer_class = ImageOutsiteRegSerializer
    queryset = ImageOutsiteReg.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]


class ImageTerritoryListView(ListAPIView, CreateAPIView):
    img_array = 'territory_img'

    serializer_class = ImageListTerritorySerializer
    """Представление списка картинок территории"""
    serializer_class = ImageTerritorySerializer
    queryset = ImageTerritory.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]

    # todo
    def post(self, request, *args, **kwargs):
        if request.data.get(self.img_array):
            serializer = ImageTerritorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            territory = serializer.instance
            print(dir(territory), 'ettbn')
            territory_id = territory.territory_id
            file_load_instance = FileLoad()
            file_load_instance.move_upload_img_for_territory(request, self.img_array, territory_id)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(f'Bad Request {self.img_array}, required field does not exist', status.HTTP_400_BAD_REQUEST)


class ImageTerritoryDetailView(RetrieveAPIView, DestroyAPIView):
    """Представление картинок определенной выездной регистрации"""
    serializer_class = ImageTerritorySerializer
    queryset = ImageTerritory.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]


class OutsiteRegistrationListView(ListAPIView, CreateAPIView):
    img_array = 'out_reg_image'

    """Представление списка выездных регистраций"""
    serializer_class = OutsiteRegistrationListSerializer
    queryset = OutsiteRegistration.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data.get(self.img_array):
            serializer = OutsiteRegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            reg = serializer.instance
            out_reg_id = reg.id
            file_load_instance = FileLoad()
            file_load_instance.move_upload_img_for_out_reg(request, self.img_array, out_reg_id)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(f'Bad Request {self.img_array}, required field does not exist', status.HTTP_400_BAD_REQUEST)

    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]


class OutsiteRegistrationDetailView(RetrieveAPIView, DestroyAPIView):
    """Представление определенной выездной регистрации"""
    serializer_class = OutsiteRegistrationSerializer
    queryset = OutsiteRegistration.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly | BrideReadonlyPermission | VendorCanCreatePermission]
