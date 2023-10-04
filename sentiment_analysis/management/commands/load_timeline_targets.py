from django.core.management import BaseCommand


class LoadTargets(BaseCommand):

    def __init__(self):
        self.categories = [
            'news','celebrities','stocks','politicians','environment','economy','education'
        ]


    def handle(self):
        pass

