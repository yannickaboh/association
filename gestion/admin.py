from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from . import models
from django.conf import settings

# Register your models here.

class TypeClientAdmin(admin.ModelAdmin):
	list_display   = ('libelle', 'description', 'created_at', 'updated_at', 'created_at', 'ajoute_par')
	list_filter    = ('libelle', 'description', 'created_at', 'updated_at', 'created_at', 'ajoute_par')
	date_hierarchy = 'created_at'
	ordering       = ('created_at', 'updated_at')
	search_fields  = ('libelle', 'description', 'created_at', 'updated_at', 'created_at', 'ajoute_par')

	def save_model(self, request, obj, form, change):
		if getattr(obj, 'ajoute_par', None) is None:
			obj.ajoute_par = request.user
		obj.save()




admin.site.unregister(User)
admin.site.register(models.TypeClient, TypeClientAdmin)
admin.site.register(models.Client, )
admin.site.register(models.Secteur, )
admin.site.register(models.Tiers, )
admin.site.register(models.Mandataire, )
admin.site.register(models.Compte, )
admin.site.register(models.Statut, )
admin.site.register(models.TypeCompte, )
admin.site.register(models.Fournisseur, )
admin.site.register(models.Agence, )
admin.site.register(models.Banque, )
admin.site.register(models.Agent, )
admin.site.register(models.Fonction, )
admin.site.register(models.TypeBanque, )
admin.site.register(models.Caisse, )
admin.site.register(models.Traitement, )
admin.site.register(models.Depot, )
admin.site.register(models.Retrait, )
admin.site.register(models.Ouverture, )
admin.site.register(models.Fermeture, )
admin.site.register(models.Simple, )
admin.site.register(models.Deroge, )
admin.site.register(models.Operation, )
admin.site.register(models.TypeCompteTiers, )
admin.site.register(models.CompteTiers, )
admin.site.register(models.Frais, )
admin.site.register(models.Prestation, )
admin.site.register(models.Carte, )
admin.site.register(models.Cheque, )
admin.site.register(models.Produit, )
admin.site.register(models.Devise, )
admin.site.register(models.Service, )
admin.site.register(models.Souscription, )
admin.site.register(models.TypeSouscription, )
admin.site.register(models.Livraison, )
admin.site.register(models.Virement, )
admin.site.register(models.Mad, )
admin.site.register(models.RemiseCheque, )
admin.site.register(models.Pret, )
admin.site.register(models.DetailPret, )
admin.site.register(models.TypePret, )
admin.site.register(models.Engagement, )