from django.core.management import BaseCommand
from users.models import User


class SeedUsers(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__()
        admin, updated = User.objects.update_or_create(
            first_name='Shane',
            last_name='Dalton',
            email='shanemdalton@gmail.com',
            is_superuser=True,
        )
        if not updated:
            admin.set_password('passworddrowssap')

    def handle(self):
        SeedUsers()
