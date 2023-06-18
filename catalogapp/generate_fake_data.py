import faker.providers
from faker import Faker
from catalogapp.models import Location, Kitchen, Event, Place, TypeArea, Area, ImageArea, ImagePlace

fake = Faker(['ru_RU'])


class CategoryProvider(faker.providers.BaseProvider):
    def categories(self):
        category = [
            'Площадки и банкетные залы',
            'Дворцы бракосочетания',
            'Отели'
        ]
        return self.random_element(category)


class LocationProvider(faker.providers.BaseProvider):
    def locations(self):
        location = ['Около моря',
                    'Около реки',
                    'За городом',
                    'В городе',
                    'В центре города',
                    'В лесу'
                    'Около озера'
                    'В горах'
                    ]
        return self.random_element(location)


class KitchenProvider(faker.providers.BaseProvider):
    def kitchen(self):
        kitchen_type = [
            'Европейская',
            'Азиатская',
            'Русская',
            'Кавказская',
            'Итальянская',
            'Японская',
            'Корейская',
            'Другая'
        ]
        return self.random_element(kitchen_type)


class EventProvider(faker.providers.BaseProvider):
    def event(self):
        event_category = (
            'Свадьба',
            'День рождения',
            'Новый год',
            'Фуршет',
            'Мальчишник',
            'Девичник',
            'Корпоратив',
            'Праздничный банкет',
            'Выпускной',
        )
        return self.random_element(event_category)


class PlaceProvider(faker.providers.BaseProvider):
    def scheme_payments(self):
        scheme_payment = [
            'Аренда зала + банкет',
            'Только банкет',
            'Только зал'
        ]
        return self.random_element(scheme_payment)


class MetroProvider(faker.providers.BaseProvider):  # check
    "Генерирует станции Метро"

    def generate_metro_station_addresses(self):
        addresses = []
        address = f"{fake.street_address()} {fake.city()}"
        addresses.append(address)
        return self.random_element(addresses)


class PaymentProvider(faker.providers.BaseProvider):

    #   Способ оплаты

    def payment_scheme(self):
        schemes = ['Visa', 'MasterCard', 'Cash', 'BTC']
        return self.random_element(schemes)


class TypeAreaProvider(faker.providers.BaseProvider):
    def area(self):
        areas = [
            'Банкетный зал',
            'Шатер',
            'Веранда',
            'Яхт-клуб',
            'Теплоход',
            'Лофт',
            'Усадьба',
            'Ресторан',
            'Кафе',
            'База отдыха',
            'Коттедж',
            'Отель',
            'Замок',
            'Загородный клуб',
            'Столовая',
        ]
        return self.random_element(areas)


""" Генерация фейк данных для  моделей """

def generate_location(count):
    """Добавление фейковых Локаций из существующих Choices"""
    fake.add_provider(LocationProvider)
    for _ in range(count):
        locations = Location.objects.create(
            location=fake.locations()
        )
        locations.save()


def generate_kitchen(count):
    """Добавление фейковых Kitchen из существующих Choices"""
    fake.add_provider(KitchenProvider)
    for _ in range(count):
        kitchen_types = Kitchen.objects.create(
            kitchen=fake.kitchen()
        )
        kitchen_types.save()


def generate_event(count):
    """Добавление фейковых Events из существующих Choices"""
    fake.add_provider(EventProvider)
    for _ in range(count):
        events = Event.objects.create(
            event=fake.event()
        )
        events.save()


def generate_place(count):
    """Добавление фейковых данных в модель Place"""
    fake.add_provider(EventProvider)
    fake.add_provider(MetroProvider)
    fake.add_provider(PaymentProvider)
    for _ in range(count):
        places = Place.objects.create(

            title=fake.sentence(nb_words=3)[:-1],
            city=fake.city(),
            metro=fake.generate_metro_station_addresses(),
            address=fake.address(),
            start_time=fake.time(),
            finish_time=fake.time(),
            fireworks=fake.pybool(),
            children_kitchen=fake.pybool(),
            alco=fake.pybool(),
            scheme_of_payment=fake.payment_scheme(),
            corkage_fee=fake.pybool(),
            payment_of_alco=fake.random_int(min=1000, max=5000),
            lease_extension=fake.pybool(),
            lease_extension_price=fake.random_int(min=1, max=1000),
            average_check=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
            description=fake.text(max_nb_chars=30),

        )
        places.location.set(Location.objects.filter(pk__in=[1, 2, 3, 4, 5, 6, 7, 8]))  # check
        places.kitchen.set(Kitchen.objects.filter(pk__in=[1, 2, 3, 4, 5, 6, 7, 8]))
        places.event.set(Event.objects.filter(pk__in=[1, 2, 3, 4, 5, 6, 7, 8, ]))

        places.save()


def generate_type_area(count):
    """ Генерирует Тип площадки """
    fake.add_provider(TypeAreaProvider)
    for _ in range(count):
        type_areas = TypeArea.objects.create(
            type_area=fake.area()
        )
        type_areas.save()


def generate_area(count):
    for _ in range(count):
        areas = Area.objects.create(
            title=fake.sentence(nb_words=3)[:-1],
            type_area=TypeArea.objects.order_by('?').first(),
            min_capacity=fake.random_int(min=1, max=10),
            max_capacity=fake.random_int(min=10, max=30),
            color_hall=fake.color_name(),
            separate_entrance=fake.pybool(),
            sale=fake.random.uniform(10, 80),
            min_price_banquet=fake.random_int(min=100, max=1000),
            min_price_rent=fake.pyint(min_value=10, max_value=70),
            deposit=fake.pyint(min_value=50),
            detail_location=fake.text(max_nb_chars=15),
            place=Place.objects.order_by('?').first(),

        )
        areas.save()


def generate_image_area(count):
    for _ in range(count):
        image_area = ImageArea.objects.create(
            area=Area.objects.order_by('?').first(),
            image=fake.image_url()
        )
        image_area.save()


def generate_image_place(count):
    for _ in range(count):
        image_place = ImagePlace.objects.create(
            place=Place.objects.order_by('?').first(),
            image=fake.image_url()
        )
        image_place.save()
