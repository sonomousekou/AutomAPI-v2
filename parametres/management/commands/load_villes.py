import json
from django.core.management.base import BaseCommand
from parametres.models import Region, Pays, Ville
import os

# fonction pour vider la table avant de la remplir
def clear_data_p():
    Ville.objects.all().delete()

class Command(BaseCommand):


    help = 'Remplit la table Region avec des données de test'

    def handle(self, *args, **kwargs):

        self.stdout.write('Vidage de la table Ville...')
        clear_data_p()
    
        filename = 'villes.json'
        file_path = os.path.join('parametres', 'data', filename)


        # Charger les données du fichier JSON
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Importer chaque ville
        for ville_data in data:
            # Récupérer le code de la région
            region_code = ville_data['region']

            # Vérifier si la région existe dans la base de données
            try:
                region = Region.objects.get(code=region_code)
            except Region.DoesNotExist:
                self.stderr.write(self.style.ERROR(f"La région avec le code {region_code} n'existe pas dans la base de données. La ville {ville_data['nom']} ne sera pas importée."))
                continue

            # Récupérer le code du pays
            pays_code = ville_data['pays']

            # Vérifier si le pays existe dans la base de données
            try:
                pays = Pays.objects.get(code=pays_code)
            except Pays.DoesNotExist:
                self.stderr.write(self.style.ERROR(f"Le pays avec le code {pays_code} n'existe pas dans la base de données. La ville {ville_data['nom']} ne sera pas importée."))
                continue

            # Créer la ville
            if Ville.objects.filter(code=ville_data['code']).exists():
                self.stdout.write(self.style.WARNING(f"Ville {ville_data['nom']} existe déjà"))
            else:
                ville = Ville(
                code=ville_data['code'],
                nom=ville_data['nom'],
                description=ville_data.get('description'),
                region=region,
                pays=pays,
                )
                ville.save()
                self.stdout.write(self.style.SUCCESS(f"La ville {ville_data['nom']} a été importée avec succès."))
