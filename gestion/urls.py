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


]