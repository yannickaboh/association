from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from .forms import UserForm, ClientForm, TypeClientForm, CompteForm
import re
from django.db.models import Q

from .models import Client, Compte

# Create your views here.



def index(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('gestion:acceuil')
			else:
				return render(request, 'gestion/pages/index.html', {'error_message': 'Votre compte a été désactivé'})
		else:
			return render(request, 'gestion/pages/index.html', {'error_message': 'Paramètres Invalides'})
	return render(request, 'gestion/pages/index.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('gestion:index')



def acceuil(request):
	return render(request, 'gestion/pages/acceuil.html', {})



# Medicament CRUD
class ClientList(ListView):
	model = Client

class ClientCreate(CreateView):
	model = Client
	form_class = ClientForm
	success_url = reverse_lazy('gestion:client_list')

class ClientUpdate(UpdateView):
	model = Client
	form_class = ClientForm
	success_url = reverse_lazy('gestion:client_list')

class ClientDelete(DeleteView):
	model = Client
	success_url = reverse_lazy('gestion:client_list')



# Medicament CRUD
class CompteList(ListView):
	model = Compte

class CompteCreate(CreateView):
	model = Compte
	form_class = CompteForm
	success_url = reverse_lazy('gestion:compte_list')

class CompteUpdate(UpdateView):
	model = Compte
	form_class = CompteForm
	success_url = reverse_lazy('gestion:compte_list')

class CompteDelete(DeleteView):
	model = Compte
	success_url = reverse_lazy('gestion:compte_list')



