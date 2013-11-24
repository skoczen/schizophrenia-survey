from django.core.cache import cache
from django.core.management.base import BaseCommand
from utils.factory import Factory
from survey.models import NEXT_SURVEY_PATH_KEY


class Command(BaseCommand):

    def handle(self, *args, **options):
        cache.delete(NEXT_SURVEY_PATH_KEY)
        for i in range(100):
            Factory.survey_path(order=i)
