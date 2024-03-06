from django.core.cache import cache
from django.core.management import BaseCommand

from core.utils.console import Console


class Command(BaseCommand):
    help = "Clear all caches"

    def handle(self, *args, **options):
        cache.clear()
        Console.success("Cache cleared successfully")
