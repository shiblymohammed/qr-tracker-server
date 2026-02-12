from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **options):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'zebacalicut')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@zebacalicut.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'Zeba.calicut@2026')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists'))
