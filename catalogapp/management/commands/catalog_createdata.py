from django.core.management.base import BaseCommand
from catalogapp.generate_fake_data import generate_location,generate_kitchen,generate_event,\
    generate_place,generate_type_area,generate_area,generate_image_area,generate_image_place


class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_location(10)
        generate_kitchen(10)
        generate_event(10)
        generate_place(10)
        generate_type_area(10)
        generate_area(10)
        generate_image_area(10)
        generate_image_place(10)
        print('Completed')
