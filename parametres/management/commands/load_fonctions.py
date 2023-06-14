from django.core.management.base import BaseCommand
from parametres.models import Fonction

class Command(BaseCommand):
    help = 'Load initial data for Fonction model'

    def handle(self, *args, **options):
        # Define the list of Fonction objects to create
        fonctions = [
            Fonction(nom='Directeur général'),
            Fonction(nom='Directeur des ressources humaines'),
            Fonction(nom='Directeur financier'),
            Fonction(nom='Responsable marketing'),
            Fonction(nom='Ingénieur logiciel'),
            Fonction(nom='Analyste financier'),
            Fonction(nom='Chargé de clientèle'),
            Fonction(nom='Responsable de production'),
            Fonction(nom='Chef de projet'),
            Fonction(nom='Technicien de maintenance'),
        ]

        # Create the Fonction objects
        Fonction.objects.bulk_create(fonctions)

        self.stdout.write(self.style.SUCCESS('Fonctions have been loaded successfully'))
