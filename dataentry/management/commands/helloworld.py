from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prints Hello World"

    def handle(self, *args, **kwargs):
        # we write the logic
        # testing git
        self.stdout.write('Hello World')