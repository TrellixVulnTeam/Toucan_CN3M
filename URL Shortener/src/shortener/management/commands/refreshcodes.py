__author__ = 'Alkesh'
from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL

class Command(BaseCommand):
    help = "Refreshes all the shortcodes"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('--items',type=int)

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcodes(items=options['items'])