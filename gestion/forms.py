from django import forms
from django.contrib.auth.models import User
from .models import Client, TypeClient, Compte
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        exclude = ['created_at', 'updated_at', 'ajoute_par']


class TypeClientForm(forms.ModelForm):

    class Meta:
        model = TypeClient
        fields = ['libelle', 'description']


class ClientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'client-form'
        # Tu définis la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        # Tu crées l'affichage de ton formulaire
        self.helper.layout = Layout(
            # Le formulaire va contenir 3 onglets
            TabHolder(
                # Premier onglet
                Tab(
                    # Label de l'onglet
                    'Général',
                    # Liste des champs du modèle à afficher dans l'onglet
                    'noms',
                    'prenoms',
                    'datenaissance',
                    'photo',
                    # Tu rajoutes un bouton "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % "Suivant",
                        type='button',
                        css_class='btn-warning col-md-offset-9 btnNext',
                    )

                ),
                # Deuxième onglet
                Tab(
                    # Label de l'onglet
                    'Informations',
                    # Liste des champs à afficher
                    'typeclient',
                    'email',
                    'phone',
                    'profession',
                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Précédent',
                        type='button',
                        css_class='btn-primary btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Suivant',
                        type='button',
                        css_class='btn-warning col-md-offset-8 btnNext',
                    )
                ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Autres',
                    # Liste des champs à afficher dont les champs supplémentaires
                    'adresse',
                    'ville',
                    'nationalite',
                    'quartier',
                    # Tu rajoutes des boutons "Précédent" et "Valider"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % "Précédent",
                        type='button',
                        css_class='btn-warning btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-ok" \
                        aria-hidden="true"></span> %s' % "Valider",
                        type='submit',
                        css_class='btn-success col-md-offset-8'
                    )
                ),
            ),
        )

    class Meta:
        # Tu définis le modèle utilisé
        model = Client
        exclude = ['created_at', 'updated_at', 'ajoute_par']



class CompteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'compte-form'
        # Tu définis la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        # Tu crées l'affichage de ton formulaire
        self.helper.layout = Layout(
            # Le formulaire va contenir 3 onglets
            TabHolder(
                # Premier onglet
                Tab(
                    # Label de l'onglet
                    'Compte',
                    # Liste des champs du modèle à afficher dans l'onglet
                    'typecompte',
                    'numero',
                    'ouverture',
                    'cloture',
                    # Tu rajoutes un bouton "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % "Suivant",
                        type='button',
                        css_class='btn-warning col-md-offset-9 btnNext',
                    )

                ),
                # Deuxième onglet
                Tab(
                    # Label de l'onglet
                    'Conditions arrêtées',
                    # Liste des champs à afficher
                    'intitule',
                    'statut',
                    'matricule',
                    'montancartone',
                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Précédent',
                        type='button',
                        css_class='btn-primary btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Suivant',
                        type='button',
                        css_class='btn-warning col-md-offset-8 btnNext',
                    )
                ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Autres',
                    # Liste des champs à afficher dont les champs supplémentaires
                    'numcpte',
                    'decouvertauto',
                    'debut',
                    'fin',
                    # Tu rajoutes des boutons "Précédent" et "Valider"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % "Précédent",
                        type='button',
                        css_class='btn-warning btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-ok" \
                        aria-hidden="true"></span> %s' % "Valider",
                        type='submit',
                        css_class='btn-success col-md-offset-8'
                    )
                ),
            ),
        )

    class Meta:
        # Tu définis le modèle utilisé
        model = Compte
        exclude = ['created_at', 'updated_at', 'ajoute_par']