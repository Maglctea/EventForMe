from django.db import models

from authapp.models import User


class TypePlace(models.Model):
    """Тип площадки"""
    sites = 'site'
    zags = 'zags'
    presenters = 'present'
    photographer = 'photo'
    designer = 'design'
    organization = 'org'
    dj = 'dj'
    invitations = 'invit'
    videographer = 'video'
    floristry = 'flor'
    stylists = 'style'
    visagists = 'visage'
    music_group = 'music'
    ch_anim = 'anim'
    choreographers = 'chor'
    show_program = 'show'
    light_sound = 'las'
    beauty_and_health = 'bah'
    cakes_and_desserts = 'cad'
    wedding_dress = 'weddr'
    mens_suits = 'mensuit'
    wedding_rings = 'wedri'
    bridesmaid_dresses = 'brsmdr'
    transport = 'transp'
    barmens = 'barmen'
    fireworks = 'firew'

    type_places = (
        (sites, 'Площадки'),
        (zags, 'Дворец бракосочетания'),
        (presenters, 'Ведущие'),
        (photographer, 'Фотографы'),
        (designer, ' Оформление и декор'),
        (organization, 'Организаторы'),
        (dj, 'Диджеи'),
        (invitations, 'Приглашения'),
        (videographer, 'Видеографы'),
        (floristry, ' Флористика и букеты'),
        (stylists, 'Стилисты'),
        (visagists, 'Визажисты'),
        (music_group, 'Музыкальные группы'),
        (ch_anim, 'Детские аниматоры'),
        (choreographers, 'Хореографы'),
        (show_program, 'Шоу-программа'),
        (light_sound, 'Свет и звук'),
        (beauty_and_health, 'Красота и здоровье'),
        (cakes_and_desserts, 'Торты и десерты'),
        (wedding_dress, 'Свадебные платья'),
        (mens_suits, 'Мужские костюмы'),
        (wedding_rings, 'Обручальные кольца'),
        (bridesmaid_dresses, 'Платья подружек невесты'),
        (transport, 'Транспорт'),
        (barmens, 'Бармены'),
        (fireworks, 'Фейерверки'),
    )
    type_place = models.CharField(verbose_name='Тип площадки', choices=type_places, max_length=7, )

    def __str__(self):
        return self.get_type_place_display()

    class Meta:
        verbose_name = 'Тип площадки'
        verbose_name_plural = 'Типы площадок'


class Location(models.Model):
    """Локации"""
    SEA = 'sea'
    RIVER = 'river'
    OUT_CITY = 'outc'
    IN_CITY = 'inc'
    IN_CENTER_CITY = 'icc'
    IN_FOREST = 'forest'
    LAKE = 'lake'
    IN_MOUNTAINS = 'imt'
    location_place = (
        (SEA, 'Около моря'),
        (RIVER, 'Около реки'),
        (OUT_CITY, 'За городом'),
        (IN_CITY, 'В городе'),
        (IN_CENTER_CITY, 'В центре города'),
        (IN_FOREST, 'В лесу'),
        (LAKE, 'Около озера'),
        (IN_MOUNTAINS, 'В горах'),
    )
    location = models.CharField(verbose_name='Локация', choices=location_place, max_length=6)

    def __str__(self):
        return self.get_location_display()

    class Meta:
        verbose_name = 'Вид локации'
        verbose_name_plural = 'Виды локаций'


class Kitchen(models.Model):
    """Кухни"""
    EUROPE = 'eur'
    ASIAN = 'asia'
    RUSSIAN = 'rus'
    CAUCAZIAN = 'cau'
    ITALIAN = 'ita'
    JAPAN = 'jap'
    KOREA = 'kor'
    OTHER = 'other'
    country_kitchen = (
        (EUROPE, 'Европейская'),
        (ASIAN, 'Азиатская'),
        (RUSSIAN, 'Русская'),
        (CAUCAZIAN, 'Кавказская'),
        (ITALIAN, 'Итальянская'),
        (JAPAN, 'Японская'),
        (KOREA, 'Корейская'),
        (OTHER, 'Другая'),
    )
    kitchen = models.CharField(verbose_name='Кухни', choices=country_kitchen, max_length=5)

    def __str__(self):
        return self.get_kitchen_display()

    class Meta:
        verbose_name = 'Кухня'
        verbose_name_plural = 'Кухни'


class Event(models.Model):
    """Виды событий, которые могут быть проведены на площадке"""
    WEDDING = 'wed'
    BIRTHDAY = 'birth'
    NEW_YEAR = 'nyr'
    BUFFET = 'buf'
    BACHELOR = 'bach'
    BACHELORETTE = 'bclt'
    COMPANY = 'cmp'
    FESTIVE = 'fest'
    GRADUATION = 'grd'
    event_category = (
        (WEDDING, 'Свадьба'),
        (BIRTHDAY, 'День рождения'),
        (NEW_YEAR, 'Новый год'),
        (BUFFET, 'Фуршет'),
        (BACHELOR, 'Мальчишник'),
        (BACHELORETTE, 'Девичник'),
        (COMPANY, 'Корпоратив'),
        (FESTIVE, 'Праздничный банкет'),
        (GRADUATION, 'Выпускной'),
    )
    event = models.CharField(verbose_name='Подходит для', choices=event_category, max_length=6)

    def __str__(self):
        return self.get_event_display()

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class Features(models.Model):
    """Особенности деталей площадки"""
    GUEST_ROOM = 'guestr'
    HONEYMOON_SUITE = 'room'
    PROJECTOR = 'proj'
    TV = 'tv'
    DANCEPOL = 'dance'
    SCENE = 'scen'
    BRIDE_ROOM = 'brid'
    DRESS_ROOM = 'dress'
    PANORAMA = 'pan'
    PHOTOZONE = 'phot'

    type_features = (
        (GUEST_ROOM, 'Номер для гостей'),
        (HONEYMOON_SUITE, 'Номер для новобрачных'),
        (PROJECTOR, 'Есть проектор'),
        (TV, 'ТВ-экраны'),
        (DANCEPOL, 'Есть танцпол'),
        (SCENE, 'Есть сцена'),
        (BRIDE_ROOM, 'Есть комната невесты'),
        (DRESS_ROOM, 'Есть примерочная'),
        (PANORAMA, 'Панорамный вид'),
        (PHOTOZONE, 'Фотозона'),
    )
    type_feature = models.CharField(verbose_name='Особенности деталей площадки', max_length=6, choices=type_features)

    def __str__(self):
        return self.get_type_feature_display()

    class Meta:
        verbose_name = 'Деталь площадки'
        verbose_name_plural = 'Детали площадки'


class TypeTerritory(models.Model):
    """Территория"""
    PARKING = 'park'
    WELCOME_ZONE = 'welc'
    FIRE_SHOW = 'fire'
    FIREWORK = 'firew'
    HOTEL = 'hotel'
    KIDS_ZONE = 'kids'
    PHOTOZONE = 'phot'
    REGISTRATION = 'reg'
    PANORAMA = 'pan'
    GUESTS_HOTEL = 'guesth'
    type_territories = (
        (PARKING, 'Своя парковка'),
        (WELCOME_ZONE, 'Welcome-зона'),
        (FIRE_SHOW, 'Место под фаер-шоу'),
        (FIREWORK, 'Можно фейерверк'),
        (HOTEL, 'Отель рядом'),
        (KIDS_ZONE, 'Детская игровая зона'),
        (PHOTOZONE, 'Фотозона'),
        (REGISTRATION, 'С выездной регистрацией'),
        (PANORAMA, 'Панорамный вид'),
        (GUESTS_HOTEL, 'Отель для гостей')
    )
    type_territory = models.CharField(choices=type_territories, max_length=6, verbose_name='территория')

    def __str__(self):
        return self.get_type_territory_display()

    class Meta:
        verbose_name = 'Территория'
        verbose_name_plural = 'Территории'


class Place(models.Model):
    """Площадки"""
    cover_place = models.ImageField(upload_to='cover_place/', verbose_name='Обложка', null=True, blank=True)
    type_place = models.ManyToManyField(TypePlace, verbose_name='Тип площадки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Id владельца', null=True, blank=True,
                             related_name='users')
    title = models.CharField(verbose_name='Название площадки', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=20)
    metro = models.CharField(verbose_name='Станция метро', max_length=20, null=True, blank=True)
    address = models.CharField(verbose_name='Адресс', max_length=300)
    longitude = models.FloatField(verbose_name='Долгота')
    width = models.FloatField(verbose_name='Широта')
    id_yandex = models.CharField(verbose_name='Id на яндекс картах', null=True, blank=True, max_length=50)
    start_time = models.TimeField(verbose_name='Начало работы')
    finish_time = models.TimeField(verbose_name='Конец работы')
    location = models.ManyToManyField(Location, verbose_name='Локации')
    fireworks = models.BooleanField(verbose_name='Можно запустить фейерверки?')
    kitchen = models.ManyToManyField(Kitchen, verbose_name='Кухни')
    children_kitchen = models.BooleanField(verbose_name='Детское меню', null=True, blank=True, default=False)
    alco = models.BooleanField(verbose_name='Можно принести свой алкоголь?', null=True, blank=True, default=True)
    payment_of_alco = models.PositiveSmallIntegerField(verbose_name='Плата за пронос вашего алкоголя')
    lease_extension = models.BooleanField(verbose_name='Продление аренды')
    lease_extension_price = models.PositiveSmallIntegerField(verbose_name='Cтоимость продления аренды')
    average_check = models.PositiveSmallIntegerField(verbose_name='Средний чек')
    event = models.ManyToManyField(Event, verbose_name='Подходит для')
    description = models.TextField(verbose_name='Описание площадки')
    parking = models.PositiveSmallIntegerField(verbose_name='Вместимость парковки', null=True, blank=True)
    type_feature = models.ManyToManyField(Features, verbose_name='Особенности деталей площадки')
    max_serving = models.PositiveSmallIntegerField(verbose_name='Сколько обслуживает один официант')
    type_territory = models.ManyToManyField(TypeTerritory, verbose_name='Территории', null=True, blank=True)

    territory_desc = models.CharField(verbose_name='Описание территории', null=True, blank=True, max_length=1000)

    def __str__(self):
        return f'Title {self.title} '

    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'


class WelcomeZone(models.Model):
    """Welcome zone"""
    welcome_desc = models.CharField(verbose_name='Описание welcome зоны', null=True, blank=True, max_length=1000)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='К какой площадке относится',
                              related_name='welcome_zones')

    def __str__(self):
        return f'{self.welcome_desc}'

    class Meta:
        verbose_name = 'welcome - зона'
        verbose_name_plural = 'welcome - зоны'


class OutsiteRegistration(models.Model):
    """Выездная регистрация"""
    outreg_price = models.PositiveSmallIntegerField(verbose_name='Стоимост выездной регистрации')
    outreg_conditions = models.CharField(verbose_name='Условия выездной регистрации', null=True, blank=True,
                                         max_length=1000)
    outreg_include = models.CharField(verbose_name='Входит в выездную регистрацию', null=True, blank=True,
                                      max_length=1000)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='К какой площадке относится',
                              related_name='outsites_reg')

    def __str__(self):
        return f'{self.outreg_include}'

    class Meta:
        verbose_name = 'Выездная регистрация'
        verbose_name_plural = 'Выездные регистрации'


class TypeArea(models.Model):
    """Вид площадки"""
    BANQUET_HALL = 'bqh'
    TENT = 'tent'
    VERANDA = 'vrnd'
    YACHT_CLUB = 'ycc'
    MOTOR_SHIP = 'mts'
    LOFT = 'loft'
    MANOR = 'mnr'
    RESTAURANT = 'rsrn'
    CAFE = 'cafe'
    REC_CENTER = 'rct'
    COTTAGE = 'ctg'
    HOTEL = 'htl'
    CASTLE = 'cst'
    COUNTRY_CLUB = 'cntc'
    CANTEEN = 'cntn'
    area_type = (
        (BANQUET_HALL, 'Банкетный зал'),
        (TENT, 'Шатер'),
        (VERANDA, 'Веранда'),
        (YACHT_CLUB, 'Яхт-клуб'),
        (MOTOR_SHIP, 'Теплоход'),
        (LOFT, 'Лофт'),
        (MANOR, 'Усадьба'),
        (RESTAURANT, 'Ресторан'),
        (CAFE, 'Кафе'),
        (REC_CENTER, 'База отдыха'),
        (COTTAGE, 'Коттедж'),
        (HOTEL, 'Отель'),
        (CASTLE, 'Замок'),
        (COUNTRY_CLUB, 'Загородный клуб'),
        (CANTEEN, 'Столовая'),
    )
    type_area = models.CharField(verbose_name='Тип площадки', choices=area_type, max_length=5)

    def __str__(self):
        return self.get_type_area_display()

    class Meta:
        verbose_name = 'Вид места'
        verbose_name_plural = 'Виды мест'


class Area(models.Model):
    """Место на площадке"""
    BANQUET_HALL = 'bah'
    BANQUET = 'ban'
    HALL = 'hall'
    scheme_payment = (
        (BANQUET_HALL, 'Аренда зала + банкет'),
        (BANQUET, 'Только банкет'),
        (HALL, 'Только зал'),
    )
    WHITE = 'white'
    PINK = 'pink'
    RED = 'red'
    ORANGE = 'orange'
    YELLOW = 'yellow'
    GREEN = 'green'
    LIGHT_BLUE = 'lblue'
    BLUE = 'blue'
    PURPLE = 'purple'
    BEIGE = 'beige'
    color_halls = (
        (WHITE, 'Белый'),
        (PINK, 'Розовый'),
        (RED, 'Красный'),
        (ORANGE, 'Оранжевый'),
        (YELLOW, 'Желтый'),
        (GREEN, 'Зеленый'),
        (LIGHT_BLUE, 'Голубой'),
        (BLUE, 'Синий'),
        (PURPLE, 'Фиолетовый'),
        (BEIGE, 'Бежевый'),
    )
    title = models.CharField(verbose_name='Заголовки', max_length=50)
    cover_area = models.ImageField(upload_to='cover_area/', verbose_name='Обложка', null=True, blank=True)
    type_area = models.ForeignKey(TypeArea, on_delete=models.SET_NULL, verbose_name='Тип площадки', null=True,
                                  blank=True)
    min_capacity = models.PositiveSmallIntegerField(verbose_name='Минимальная вместимость')
    max_capacity = models.PositiveSmallIntegerField(verbose_name='Максимальная вместимость')
    color_hall = models.CharField(verbose_name='Цвет зала', max_length=6, choices=color_halls)
    separate_entrance = models.BooleanField(verbose_name='Отдельный вход', default=False, null=True, blank=True)
    sale = models.CharField(verbose_name='Скидка или подарок', null=True, blank=True, max_length=100)
    min_price_banquet = models.PositiveSmallIntegerField(verbose_name='Минимальная цена банкета')
    min_price_rent = models.PositiveSmallIntegerField(verbose_name='Минимальная цена аренды')
    deposit = models.PositiveSmallIntegerField(verbose_name='Предоплата')
    scheme_of_payment = models.CharField(verbose_name='Схема оплаты', choices=scheme_payment, max_length=4)
    detail_location = models.CharField(verbose_name='Дополнительная информация', max_length=1000)
    reserved_days = models.DateField(verbose_name='Зарезервированная дата', null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Относится к какой площадке',
                              related_name='areas')

    def __str__(self):
        return f'Area {self.title} - place {self.min_price_banquet}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class ImageTerritory(models.Model):
    """Картинки территории"""
    image = models.ImageField(verbose_name='Фото территории', upload_to='image_territories/')
    territory = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Площадка',
                                  related_name='image_territory')

    class Meta:
        verbose_name = 'Картинка территории'
        verbose_name_plural = 'Картинки территории'


class ImageOutsiteReg(models.Model):
    """Картинки Выездной регистрации"""
    image = models.ImageField(verbose_name='Фото территории', upload_to='image_territories/')
    outsite_reg = models.ForeignKey(OutsiteRegistration, on_delete=models.CASCADE, verbose_name='Выездная регистрация',
                                    related_name='images_out_reg')

    class Meta:
        verbose_name = 'Картинка выездной регистрации'
        verbose_name_plural = 'Картинки выездной регистрации'


class ImageArea(models.Model):
    """Картинки места"""
    image = models.ImageField(verbose_name='Фото места', upload_to='image_area/')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Место', related_name='images_area')

    class Meta:
        verbose_name = 'Картинка места'
        verbose_name_plural = 'Картинки мест'


class ImagePlace(models.Model):
    """Картинки площадки"""
    image = models.ImageField(verbose_name='Фото площадки', upload_to='image_place/')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Площадка', related_name='images_place')

    class Meta:
        verbose_name = 'Картинка площадки'
        verbose_name_plural = 'Картинки площадок'


class ImageWelcomeZone(models.Model):
    """Картинки велком зоны"""
    image = models.ImageField(verbose_name='Фото  welcome зоны', upload_to='image_welcome/')
    welcome_zone = models.ForeignKey(WelcomeZone, on_delete=models.CASCADE, verbose_name='Welcome-зона',
                                     related_name='images_welcome')

    class Meta:
        verbose_name = 'Картинка welcome зоны'
        verbose_name_plural = 'Картинки welcome зоны'


class ImageWedding(models.Model):
    """Картинки прошедших свадеб"""
    image = models.ImageField(verbose_name='Фото прошедших свадеб', upload_to='image_wedding/')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место проведения',
                              related_name='images_wedding')

    class Meta:
        verbose_name = 'Картинка прошедшeй свадьбы'
        verbose_name_plural = 'Картинки прошедших свадеб'
