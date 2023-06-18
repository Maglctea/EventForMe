from django.core.management.base import BaseCommand
from authapp.generate_auth_fake_data import generate_user_fake_data


class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_user_fake_data(10)
        print('Completed')
