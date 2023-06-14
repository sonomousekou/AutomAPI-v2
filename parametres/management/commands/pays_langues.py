import os
import json
from django.core.management.base import BaseCommand
from parametres.models import LanguePays, Pays

# fonction pour vider la table avant de la remplir
def clear_data_l():
    LanguePays.objects.all().delete()

# fonction pour vider la table avant de la remplir
def clear_data_p():
    Pays.objects.all().delete()

class Command(BaseCommand):
    help = 'Importe des pays depuis un fichier JSON'

    # def add_arguments(self, parser):
    #     parser.add_argument('filename', type=str, help='Le nom du fichier JSON à importer')

    def handle(self, *args, **options):
        # filename = options['filename']
        filename = 'pays.json'
        file_path = os.path.join('parametres', 'data', filename)

        self.stdout.write('Vidage de la table Langue...')
        clear_data_l()

        self.stdout.write('Vidage de la table Pays...')
        clear_data_p()

        with open(file_path, 'r') as f:
            data = json.load(f)

        # print(pays_data)
        # Ajouter chaque pays à la table
        for pays_data in data:
            if Pays.objects.filter(code=pays_data['code']).exists():
                self.stdout.write(self.style.WARNING(f'Pays "{pays_data}" existe déjà'))
            else:
                pays, created = Pays.objects.get_or_create(
                    nom=pays_data['nom'],
                    code=pays_data['code'],
                    indicatif=pays_data['indicatif']
                )
                self.stdout.write(self.style.SUCCESS(f'Pays "{pays_data}" ajouté avec succès'))

            # Ajouter les langues du pays
            for langue_data in pays_data['langues']:
                # Vérifier si la langue existe déjà dans la base de données
                if LanguePays.objects.filter(code=langue_data['code'] ).exists() and LanguePays.objects.filter(nom=langue_data['nom'] ).exists():
                    langue = LanguePays.objects.get(nom=langue_data['nom'])
                else:
                    langue = LanguePays.objects.create(
                        nom=langue_data['nom'],
                        code=langue_data['code']
                    )
                    if 'description' in langue_data:
                        langue.description = langue_data['description']
                        langue.save()

                pays.langues.add(langue)

        self.stdout.write(self.style.SUCCESS('Les données de pays ont été importées avec succès !'))

    