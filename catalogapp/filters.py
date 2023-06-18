from django_filters import rest_framework as filters

from catalogapp.models import Place


class PlaceFilter(filters.FilterSet):
    scheme_payment = filters.CharFilter(field_name='scheme_payment')
    city = filters.CharFilter(field_name='city', lookup_expr='icontains')
    place_style = filters.CharFilter(field_name='areas__type_area__type_area')
    min_average_check = filters.NumberFilter(field_name='average_check', lookup_expr='gte')
    max_average_check = filters.NumberFilter(field_name='average_check', lookup_expr='lte')
    territory = filters.CharFilter(field_name='type_territory__type_territory')
    type_feature = filters.CharFilter(field_name='type_feature__type_feature')
    alco = filters.BooleanFilter(field_name='type_feature__type_feature')
    min_capacity = filters.NumberFilter(field_name='areas__min_capacity', lookup_expr='gte')
    max_capacity = filters.NumberFilter(field_name='areas__max_capacity', lookup_expr='lte')


    class Meta:
        model = Place
        fields = ['scheme_payment']
