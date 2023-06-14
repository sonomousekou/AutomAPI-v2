import json
from django.core.management.base import BaseCommand
from parametres.models import Region, Pays
import os

class Command(BaseCommand):
    help = 'Remplit la table Region avec des données de test'

    def handle(self, *args, **kwargs):
        filename = 'regions.json'
        file_path = os.path.join('parametres', 'data', filename)


        # Charger les données du fichier JSON
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Pour chaque région dans le fichier JSON, ajouter une nouvelle entrée dans la table Region
        for region_data in data:
            code = region_data['code']
            nom = region_data['nom']
            description = region_data.get('description', None)
            pays_code = region_data['pays']

            # Trouver le pays correspondant dans la table Pays
            pays = Pays.objects.get(code=pays_code)

            # Ajouter une nouvelle entrée dans la table Region
            new_region = Region(code=code, nom=nom, description=description, pays=pays)
            new_region.save()

        self.stdout.write(self.style.SUCCESS('La table Region a été remplie avec succès !'))
