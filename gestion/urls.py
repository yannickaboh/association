from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'gestion'

urlpatterns = [

    # Administration
    url(r'^admin/', admin.site.urls),

    # Gestion


]