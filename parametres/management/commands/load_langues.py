from django.core.management.base import BaseCommand
from parametres.models import Langue

class Command(BaseCommand):
    help = 'Remplit la table Langue avec des données de test'

    def handle(self, *args, **kwargs):
        # Données à ajouter à la table
        langues = [
            {'nom': 'Français', 'code': 'fr', 'description': 'Langue française'},
            {'nom': 'Anglais', 'code': 'en', 'description': 'Langue anglaise'},
            {'nom': 'Espagnol', 'code': 'es', 'description': 'Langue espagnole'},
        ]

        # Ajouter chaque langue à la table
        for langue in langues:
            if not Langue.objects.filter(code=langue['code']).exists():
                new_langue = Langue(nom=langue['nom'], code=langue['code'], description=langue['description'])
                new_langue.save()

        self.stdout.write(self.style.SUCCESS('La table Langue a été remplie avec succès !'))
