from ...models import Words
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Save words to the database'

    def handle(self, *args, **options):
        with open("game/resources/Portuguese (Brazilian).dic", "r") as f:
            data = f.readlines()
            c_or_s_words = [d.split("/")[0].strip("\n") for d in data if d.startswith("c") or d.startswith("s")]

        for word in c_or_s_words:
            new_instance = Words(word=word)
            new_instance.save()