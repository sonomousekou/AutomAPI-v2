from django.db import models
from django.utils import timezone
import os, random
from django.utils.translation import gettext_lazy as _
import uuid

from django.contrib.auth import get_user_model
User = get_user_model()

class MyCustomManager(models.Manager):
    def all(self, is_active=True):
        queryset = super().get_queryset()
        if is_active:
            queryset = queryset.filter(is_active=True)
        return queryset

class Langue(models.Model):
    code = models.CharField(verbose_name=_("Code"), max_length=50, unique=True, null=True, blank=True)
    nom = models.CharField(verbose_name=_("Nom"), max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    objects = MyCustomManager()

    class Meta:
        ordering = ['nom']
        verbose_name = _("Langue")
        verbose_name_plural = _("Langues")

    def __str__(self):
        return self.nom


class LanguePays(models.Model):
    code = models.CharField( verbose_name = _("Code"), max_length=50, unique=True, null=True, blank=True)
    nom = models.CharField( verbose_name = _("Nom"), max_length=255, null=True, blank=True)
    description = models.TextField( verbose_name = _("Description"), null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Langue Pays")
        verbose_name_plural = _("Langues Pays")

    def __str__(self):
        return self.nom

class Pays(models.Model):
    nom = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name=_("Nom"))
    code = models.CharField(max_length=10, unique=True, null=True, blank=True, verbose_name=_("Code"))
    indicatif = models.CharField(max_length=10, null=True, blank=True, verbose_name=_("Indicatif"))
    longueur_numero = models.IntegerField(null=True, blank=True, verbose_name=_("Longueur du numéro"))
    nationnalite = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Nationalité"))
    langues = models.ManyToManyField(LanguePays, default=None, blank=True, verbose_name=_("Langues"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Pays")
        verbose_name_plural = _("Pays")

    def __str__(self):
        return self.nom
    
    def get_langues(self):
        return "\n".join([str(p) for p in self.langues.all()])

class Region(models.Model):
    code = models.CharField(max_length=5, unique=True, null=True, blank=True, verbose_name=_("Code"))
    nom = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Nom"))
    description = models.TextField( verbose_name = _("Description"), null=True, blank=True)
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Pays"))
    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Région")
        verbose_name_plural = _("Régions")

    def __str__(self):
        return self.nom
    
class Ville(models.Model):
    code = models.CharField(max_length=4, unique=True, null=True, blank=True, verbose_name=_("Code"))
    nom = models.CharField(max_length=100, verbose_name=_("Nom"))
    description = models.TextField( verbose_name = _("Description"), null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Région"))
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Pays"))
    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Ville")
        verbose_name_plural = _("Villes")

    def __str__(self):
        return self.nom

class DomaineActivite(models.Model):
    code = models.CharField(max_length=4, unique=True, null=True, blank=True, verbose_name=_("Code"))
    nom = models.CharField(max_length=200, verbose_name=_("Nom"))
    description = models.TextField( verbose_name = _("Description"), null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Domaine d'activité")
        verbose_name_plural = _("Domaines d'activité")

    def __str__(self):
        return self.nom

class Profession(models.Model):
    code = models.CharField(max_length=4, unique=True, null=True, blank=True, verbose_name=_("Code"))
    nom = models.CharField(max_length=200, verbose_name=_("Nom"))
    description = models.TextField( verbose_name = _("Description"), null=True, blank=True)
    domaine = models.ForeignKey(DomaineActivite, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Domaine d'activité"))
    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Profession")
        verbose_name_plural = _("Professions")

    def __str__(self):
        return self.nom

class Fonction(models.Model):
    code = models.CharField(max_length=4, unique=True, null=True, blank=True, verbose_name=_("Code"))
    nom = models.CharField(max_length=255, verbose_name=_("Nom"))
    domaine = models.ForeignKey(DomaineActivite, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Domaine d'activité"))
    description = models.TextField( verbose_name = _("Description"), null=True, blank=True)
    
    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Fonction")
        verbose_name_plural = _("Fonctions")

    def __str__(self):
        return self.nom

class Specialite(models.Model):
    code = models.CharField(max_length=4, unique=True, null=True, blank=True, verbose_name=_("Code"))
    nom = models.CharField(max_length=200, verbose_name=_("Titre"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    domaine = models.ForeignKey(DomaineActivite, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Domaine d'activité"))

    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Spécialité")
        verbose_name_plural = _("Spécialités")

    def __str__(self):
        return self.nom

class Autorite(models.Model):
    code = models.CharField(max_length=4, unique=True, null=True, blank=True, verbose_name=_("Code"))
    nom = models.CharField(max_length=100, verbose_name=_("Nom"))
    adresse = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("Adresse"))
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Pays"))
    description = models.TextField( verbose_name = _("Description"), null=True, blank=True)
    
    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Autorité")
        verbose_name_plural = _("Autorités")

    def __str__(self):
        return self.nom

class TypePiece(models.Model):
    code = models.CharField(max_length=4, unique=True, null=True, blank=True, verbose_name=_("Code"))
    nom = models.CharField(max_length=50, verbose_name=_("Nom"))
    description = models.TextField( verbose_name = _("Description"), null=True, blank=True)
    obligatoire = models.BooleanField(default=False, verbose_name=_("Obligatoire"))

    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Type de pièce")
        verbose_name_plural = _("Types de pièces")

    def __str__(self):
        return self.nom

class Piece(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Utilisateur"))
    type_piece = models.ForeignKey(TypePiece, on_delete=models.CASCADE, verbose_name=_("Type de pièce"))
    numero = models.CharField(max_length=50, verbose_name=_("Numéro"))
    date_delivrance = models.DateField(verbose_name=_("Date de délivrance"))
    date_expiration = models.DateField(verbose_name=_("Date d'expiration"))
    autorite_delivrance = models.ForeignKey(Autorite, on_delete=models.CASCADE, verbose_name=_("Autorité de délivrance"))
    image = models.ImageField(upload_to='Pieces/', null=True, blank=True, verbose_name=_("Image"))
    description = models.TextField( verbose_name = _("Description"), null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['-updated_at']
        verbose_name = _("Pièce")
        verbose_name_plural = _("Pièces")

    def __str__(self):
        return f"{self.type_piece} {self.numero}"

class ModePaiement(models.Model):
    code = models.CharField(max_length=4, unique=True, null=True, blank=True, verbose_name=_("Code"))
    nom = models.CharField(max_length=255, unique=True, verbose_name=_("Nom"))
    description = models.TextField( verbose_name = _("Description"), null=True, blank=True)
    image = models.ImageField(upload_to='ModesPaiement/', null=True, blank=True, verbose_name=_("Image"))
    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Mode de Paiement")
        verbose_name_plural = _("Modes de Paiement")

    def __str__(self):
        return self.nom

class JourFerie(models.Model):
    nom = models.CharField(max_length=50, verbose_name=_("Nom"))
    date = models.DateField(blank=True, null=True, verbose_name=_("Date"))
    annuel = models.BooleanField(default=True, verbose_name=_("Annuel"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))

    is_active = models.BooleanField(default=True, verbose_name=_("Est actif"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date de mise à jour"))

    class Meta:
        ordering = ['nom']
        verbose_name = _("Jour Férié")
        verbose_name_plural = _("Jours Fériés")

    def __str__(self):
        return self.nom



