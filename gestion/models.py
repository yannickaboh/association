from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission
#from django.core.urlresolvers import reverse

# Create your models here.


class TypeClient(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Types Clients'



class Client(models.Model):
	typeclient = models.ForeignKey(TypeClient,  null=True, blank=True, on_delete="cascade")
	photo = models.ImageField(default='', verbose_name="Photo de profil", null=True, blank=True, upload_to='media/users')
	noms = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Noms")
	prenoms = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Prénoms")
	datenaissance = models.DateField(verbose_name="Date de Naissance")
	email = models.EmailField(max_length=250, blank=False, unique=True, verbose_name="Email")
	phone = models.CharField(max_length=250, blank=False, unique=True, verbose_name="Téléphone")
	profession = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Profession")
	adresse = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Adresse")
	ville = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Ville")
	nationalite = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Nationalité")
	quartier = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Quartier")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.noms+' '+self.prenoms
	class Meta:
		verbose_name_plural = 'Les Clients'



class Secteur(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Secteurs'


class Mandataire(models.Model):
	photo = models.ImageField(default='', verbose_name="Photo de profil", null=True, blank=True, upload_to='media/users')
	noms = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Noms")
	prenoms = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Prénoms")
	datenaissance = models.DateField(verbose_name="Date de Naissance")
	email = models.EmailField(max_length=250, blank=False, unique=True, verbose_name="Email")
	phone = models.CharField(max_length=250, blank=False, unique=True, verbose_name="Téléphone")
	profession = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Profession")
	adresse = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Adresse")
	ville = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Ville")
	nationalite = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Nationalité")
	quartier = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Quartier")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.noms+' '+self.prenoms
	class Meta:
		verbose_name_plural = 'Les Personnes Mandataires'



class Tiers(models.Model):
	photo = models.ImageField(default='', verbose_name="Photo de profil", null=True, blank=True, upload_to='media/users')
	noms = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Noms")
	prenoms = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Prénoms")
	datenaissance = models.DateField(verbose_name="Date de Naissance")
	email = models.EmailField(max_length=250, blank=False, unique=True, verbose_name="Email")
	phone = models.CharField(max_length=250, blank=False, unique=True, verbose_name="Téléphone")
	profession = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Profession")
	adresse = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Adresse")
	ville = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Ville")
	nationalite = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Nationalité")
	quartier = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Quartier")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.noms+' '+self.prenoms
	class Meta:
		verbose_name_plural = 'Les Tierses Personnes'


class TypeCompte(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Types de Compte'


class Compte(models.Model):
	STATUT  =  ( 
        ('En Activité', 'En Activité'),
        ('En Arrêt', 'En Arrêt'),
    )
	typecompte = models.ForeignKey(TypeCompte, null=True, blank=True, on_delete="cascade", verbose_name="Nature du Compte")
	numero = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Numéro Général")
	ouverture = models.DateField(blank=False, unique=False, verbose_name="Ouverture")
	cloture = models.DateField(blank=False, unique=False, verbose_name="Clôture")
	intitule = models.CharField(max_length=250, null=True, blank=True, verbose_name="Intitulé")
	statut = models.CharField(max_length=130, choices=STATUT, default='En Activité', verbose_name="Statut du Compte")
	matricule = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Matricule Fonctionnaire")
	montancartone = models.FloatField(blank=False, unique=False, verbose_name="Montant Cartoné")
	numcpte = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Compte Intérêts")
	decouvertauto = models.FloatField(blank=False, unique=False, verbose_name="Découvert Autorisé")
	debut = models.DateField(blank=False, unique=False, verbose_name="Début")
	fin = models.DateField(max_length=250, blank=False, unique=False, verbose_name="Fin")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.numero
	class Meta:
		verbose_name_plural = 'Les Comptes'

class Statut(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Statuts'


class TypeBanque(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Types de Banque'


class Banque(models.Model):
	logo = models.ImageField(default='', verbose_name="Logo", null=True, blank=True, upload_to='media/banque')
	sigle = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Sigle")
	libelle = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Libellé")
	email = models.EmailField(max_length=250, blank=False, unique=True, verbose_name="Email")
	phone1 = models.CharField(max_length=250, blank=False, unique=True, verbose_name="Téléphone")
	phone2 = models.CharField(max_length=250, blank=False, unique=True, verbose_name="Téléphone 2")
	fax = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Fax")
	adresse = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Adresse")
	ville = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Ville")
	quartier = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Quartier")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Banques'


class Agence(models.Model):
	logo = models.ImageField(default='', verbose_name="Logo", null=True, blank=True, upload_to='media/agence')
	sigle = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Sigle")
	libelle = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Libellé")
	email = models.EmailField(max_length=250, blank=False, unique=True, verbose_name="Email")
	phone1 = models.CharField(max_length=250, blank=False, unique=True, verbose_name="Téléphone")
	phone2 = models.CharField(max_length=250, blank=False, unique=True, verbose_name="Téléphone 2")
	fax = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Fax")
	adresse = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Adresse")
	ville = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Ville")
	quartier = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Quartier")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Agences'


class Agent(models.Model):
	typeclient = models.ForeignKey(TypeClient,  null=True, blank=True, on_delete="cascade")
	photo = models.ImageField(default='', verbose_name="Photo de profil", null=True, blank=True, upload_to='media/users')
	noms = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Noms")
	prenoms = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Prénoms")
	datenaissance = models.DateField(verbose_name="Date de Naissance")
	email = models.EmailField(max_length=250, blank=False, unique=True, verbose_name="Email")
	phone = models.CharField(max_length=250, blank=False, unique=True, verbose_name="Téléphone")
	profession = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Profession")
	adresse = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Adresse")
	ville = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Ville")
	nationalite = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Nationalité")
	quartier = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Quartier")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.noms+' '+self.prenoms
	class Meta:
		verbose_name_plural = 'Les Agents'



class Fonction(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Fonctions d\'une Agence'



class Caisse(models.Model):
	numero = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Numéro de Caisse")
	solde = models.FloatField(blank=False, unique=False, verbose_name="Solde")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.numero
	class Meta:
		verbose_name_plural = 'Les Caisses'


class Traitement(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Traitements'



class Depot(models.Model):
	motif = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Motif")
	montantverse = models.FloatField( blank=False, verbose_name="Montant Versé")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.motif
	class Meta:
		verbose_name_plural = 'Dépôts'


class Retrait(models.Model):
	motif = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Motif")
	montantretire = models.FloatField( blank=False, verbose_name="Montant Retiré")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.motif
	class Meta:
		verbose_name_plural = 'Retraits'



class Ouverture(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Ouvertures'

class Fermeture(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Fermetures'


class Simple(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Simples Retraits'


class Deroge(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Retraits Dérogés'


class Operation(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Operations'


class TypeCompteTiers(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Types de Compte de Tiers'


class CompteTiers(models.Model):
	typecompte = models.ForeignKey(TypeCompte, null=True, blank=True, on_delete="cascade")
	numero = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Numéro du Compte")
	solde = models.FloatField(blank=False, unique=False, verbose_name="Solde")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.numero
	class Meta:
		verbose_name_plural = 'Les Comptes Tiers'


class Prestation(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.CharField(max_length=250, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Prestations'


class Frais(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	montantfrais = models.FloatField(blank=False, unique=False, verbose_name="Montant des Frais")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Montants des Frais'


class Carte(models.Model):
	numero = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Numéro Carte")
	solde = models.FloatField(blank=False, unique=False, verbose_name="Solde")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.numero
	class Meta:
		verbose_name_plural = 'Les Cartes'


class Cheque(models.Model):
	numero = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Numéro Compte")
	montant = models.FloatField(blank=False, unique=False, verbose_name="Montant")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.numero
	class Meta:
		verbose_name_plural = 'Les Chèques'


class RemiseCheque(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Libellé")
	valeur = models.FloatField(blank=False, unique=False, verbose_name="Remise sur Chèque")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Remises sur Chèque'



class Produit(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.TextField(blank=False, unique=False, verbose_name="Description")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Produits'


class Devise(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.TextField(blank=False, unique=False, verbose_name="Description")
	valeurcfa = models.FloatField(blank=False, unique=False, verbose_name="Valeur en Frs CFA")
	valeurus = models.FloatField(blank=False, unique=False, verbose_name="Valeur en Dollars US")
	valeureuro = models.FloatField(blank=False, unique=False, verbose_name="Valeur en Euros")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Devises'


class Service(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.TextField(blank=False, unique=False, verbose_name="Description")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Services'


class TypeSouscription(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.TextField(blank=False, unique=False, verbose_name="Description")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Types de Souscription'


class Souscription(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.TextField(blank=False, unique=False, verbose_name="Description")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Souscriptions'


class Livraison(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.TextField(blank=False, unique=False, verbose_name="Description")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Livraisons'



class Fournisseur(models.Model):
	logo = models.ImageField(default='', verbose_name="Logo", null=True, blank=True, upload_to='media/agence')
	sigle = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Sigle")
	libelle = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Libellé")
	email = models.EmailField(max_length=250, blank=False, unique=True, verbose_name="Email")
	phone1 = models.CharField(max_length=250, blank=False, unique=True, verbose_name="Téléphone")
	phone2 = models.CharField(max_length=250, blank=False, unique=True, verbose_name="Téléphone 2")
	fax = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Fax")
	adresse = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Adresse")
	ville = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Ville")
	quartier = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Quartier")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Fournisseurs'



class Virement(models.Model):
	numero = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Numéro Virement")
	montantvire = models.FloatField(blank=False, unique=False, verbose_name="Montant Virement")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.numero
	class Meta:
		verbose_name_plural = 'Les Virements'


class Mad(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.TextField(blank=False, unique=False, verbose_name="Description")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'MAD'



class DetailPret(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.TextField(blank=False, unique=False, verbose_name="Description")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Details Prêt'


class TypePret(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.TextField(blank=False, unique=False, verbose_name="Description")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Types de Prêt'




class Pret(models.Model):
	typepret = models.ForeignKey(TypePret, null=True, blank=True, editable=False, verbose_name="Type de Prêt", on_delete="cascade")
	detailpret = models.ForeignKey(DetailPret, null=True, blank=True, editable=False, verbose_name="Details Prêt", on_delete="cascade")
	motif = models.TextField(max_length=250, blank=False, unique=False, verbose_name="Libellé")
	valeur = models.FloatField(blank=False, unique=False, verbose_name="Montant Prêté")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Prêts'




class Engagement(models.Model):
	libelle = models.CharField(max_length=250, blank=False, unique=False)
	description = models.TextField(blank=False, unique=False, verbose_name="Description")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
	ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

	def __str__(self):
		return self.libelle
	class Meta:
		verbose_name_plural = 'Les Engagements'








