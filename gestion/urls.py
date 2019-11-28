from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'gestion'

urlpatterns = [

    # Administration
    url(r'^admin/', admin.site.urls),

    # Gestion
    url(r'^$', views.index, name='index'),
    url(r'^acceuil/$', views.acceuil, name='acceuil'),
    url(r'^déconnexion/$', views.logout_user, name='logout'),


    # Add, Update, Delete Medicament URLS
    url(r'^clients/$', views.ClientList.as_view(), name='client_list'),
    url(r'^creer_client/$', views.ClientCreate.as_view(), name='client_create'),
    url(r'^modifier_client/(?P<pk>\d+)/$', views.ClientUpdate.as_view(), name='client_update'),
    url(r'^supprimer_client/(?P<pk>\d+)/$', views.ClientDelete.as_view(), name='client_delete'),
    url(r'^detail_client/(?P<pk>\d+)/$', views.ClientDetailView.as_view(), name='detail_client'),


    # Add, Update, Delete Medicament URLS
    url(r'^comptes/$', views.CompteList.as_view(), name='compte_list'),
    url(r'^creer_compte/$', views.CompteCreate.as_view(), name='compte_create'),
    url(r'^modifier_compte/(?P<pk>\d+)/$', views.CompteUpdate.as_view(), name='compte_update'),
    url(r'^supprimer_compte/(?P<pk>\d+)/$', views.CompteDelete.as_view(), name='compte_delete'),
    url(r'^detail_compte/(?P<pk>\d+)/$', views.CompteDetailView.as_view(), name='detail_compte'),


]