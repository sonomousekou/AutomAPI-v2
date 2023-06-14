from django.db import models
from django.core.management.base import BaseCommand
from parametres.models import Profession

class Command(BaseCommand):
    # fonction pour vider la table avant de la remplir
    def clear_data():
        Profession.objects.all().delete()

    help = 'Initializes professions in the database'
   
    def handle(self, *args, **options):
        professions = [
            ('Avocat', 'Un professionnel du droit qui représente les clients dans les affaires juridiques.'),
            {'Acheteur', 'Responsable des achats et de la gestion des fournisseurs pour une entreprise'},
            {'Architecte', 'Conçoit et supervise la construction de bâtiments'},
            ('Banquier', 'Un professionnel qui travaille dans le secteur bancaire pour offrir des services financiers.'),
            {'Chercheur', 'Effectue des recherches dans un domaine spécifique'},
            ('Chirurgien', 'Un médecin spécialisé dans la réalisation d\'opérations chirurgicales.'),
            ('Comptable', 'Un professionnel de la comptabilité qui gère les finances des entreprises et des organisations.'),
            ('Consultant', 'Un professionnel qui offre des conseils et des expertises sur divers sujets.'),
            ('Dentiste', 'Un professionnel de la santé qui traite les problèmes dentaires.'),
            ('Développeur de logiciels', 'Un professionnel qui crée et développe des logiciels.'),
            ('Électricien', 'Un professionnel qui installe et répare les installations électriques.'),
            {'Entrepreneur', 'Crée et gère sa propre entreprise'},
            ('Enseignant', 'Un professionnel qui enseigne dans les écoles et les universités.'),
            ('Graphiste', 'Un professionnel qui conçoit des graphiques et des images pour les publications imprimées et en ligne.'),
            ('Ingénieur', 'Un professionnel qui utilise la science et la technologie pour concevoir, développer et améliorer des produits et des systèmes.'),
            ('Journaliste', 'Un professionnel qui collecte, rédige et présente des nouvelles et des informations au public.'),
            ('Kinésithérapeute', 'Un professionnel de la santé qui aide les patients à récupérer après une blessure ou une maladie.'),
            ('Médecin', 'Un professionnel de la santé qui diagnostique et traite les maladies.'),
            ('Musicien', 'Un professionnel qui joue d\'un instrument de musique ou chante.'),
            ('Pharmacien', 'Un professionnel de la santé qui prépare et distribue des médicaments.'),
            ('Photographe', 'Un professionnel qui prend des photos pour les publications imprimées et en ligne.'),
            ('Policier', 'Un professionnel qui maintient l\'ordre public et prévient la criminalité.'),
            ('Psychologue', 'Un professionnel qui étudie le comportement humain et les processus mentaux.'),
            ('Restaurateur', 'Un professionnel qui gère un restaurant ou une chaîne de restaurants.'),
        ]

        for profession in professions:
            nom, description = profession
            Profession.objects.create(nom=nom, description=description)
            self.stdout.write(self.style.SUCCESS('Profession "%s" ajoutée avec succès' % nom))