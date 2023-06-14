from django.core.management.base import BaseCommand
from parametres.models import DomaineActivite

class Command(BaseCommand):
    help = 'Populate the DomaineActivite table with initial data.'

    def handle(self, *args, **kwargs):
        domaines = [
            {'nom': 'Agriculture et Agroalimentaire', 'description': 'Domaine regroupant les activités agricoles et agroalimentaires'},
            {'nom': 'Agroalimentaire', 'description': 'Secteur lié à la production et la transformation des denrées alimentaires'},
            {'nom': 'Arts, Culture et Spectacles', 'description': 'Domaine regroupant les activités artistiques et culturelles'},
            {'nom': 'Automobile et Transport', 'description': 'Domaine regroupant les activités de transport et de l\'industrie automobile'},
            {'nom': 'Banque et Finance', 'description': 'Domaine regroupant les activités bancaires et financières'},
            {'nom': 'Bâtiment, Construction et Travaux publics', 'description': 'Domaine regroupant les activités de construction et d\'aménagement'},
            {'nom': 'Commerce et Distribution', 'description': 'Domaine regroupant les activités commerciales et de distribution'},
            {'nom': 'Communication et Marketing', 'description': 'Domaine regroupant les activités de communication et de marketing'},
            {'nom': 'Éducation et Formation', 'description': 'Domaine regroupant les activités liées à l\'enseignement et à la formation'},
            {'nom': 'Énergie et Environnement', 'description': 'Domaine regroupant les activités liées à l\'énergie et à l\'environnement'},
            {'nom': 'Industrie et Manufacture', 'description': 'Domaine regroupant les activités industrielles et manufacturières'},
            {'nom': 'Informatique et Technologie', 'description': 'Domaine regroupant les activités liées à l\'informatique et aux nouvelles technologies'},
            {'nom': 'Tourisme', 'description': 'Secteur lié aux activités touristiques et de loisirs'},
            {'nom': 'Médias et Édition', 'description': 'Domaine regroupant les activités de presse et d\'édition'},
            {'nom': 'Santé et Action sociale', 'description': 'Domaine regroupant les activités de santé et d\'action sociale'},
            {'nom': 'Services aux Entreprises', 'description': 'Domaine regroupant les activités de services aux entreprises'},
            {'nom': 'Ressources Humaines', 'description': 'Toutes les activités liées aux ressources humaines'},
            {'nom': 'Juridique', 'description': 'Toutes les activités liées au droit'},
            {'nom': 'Tourisme et Hôtellerie', 'description': 'Domaine regroupant les activités de tourisme et d\'hôtellerie'},
        ]

        for domaine in domaines:
            DomaineActivite.objects.create(nom=domaine['nom'], description=domaine['description'])

        self.stdout.write(self.style.SUCCESS('Domaines créés avec succès.'))
