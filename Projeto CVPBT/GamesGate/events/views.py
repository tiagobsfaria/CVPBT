from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from datetime import datetime

from .models import Campo, Categorie, Localizacao
from .forms import CampoForm
from .utils import get_slots

# Create your views here.

def home(request):
    categories = Categorie.objects.all()
    return render(request, 'home.html', {'categories': categories})

def get_localizacoes(request, category_id):
    localizacoes = Localizacao.objects.filter(categorie=category_id)
    localizacoes_data = [{'id': loc.id, 'title': loc.title} for loc in localizacoes]
    return JsonResponse(localizacoes_data, safe=False)




class CategorieListView(ListView):
    model = Categorie
    template_name = "categorie_list.html"

class CampoListView(ListView):
    model = Campo
    template_name = "campo_list.html"

class CampoCreateView(CreateView):
    model = Campo
    template_name = "campo_create.html"
    form_class = CampoForm
    success_url = reverse_lazy("list-campos")

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

class CampoDeleteView(DeleteView):
    model = Campo
    template_name = "campo_delete.html"

    success_url = reverse_lazy("list-campos")

class CampoEditView(UpdateView):
    model = Campo
    template_name = "campo_edit.html"
    form_class = CampoForm
    success_url = reverse_lazy("list-campos")

class CampoDetailView(DetailView):
    model = Campo
    template_name = "campo_detail.html"

class AdminPanelView(TemplateView):
    template_name = 'admin_panel.html'

class ContactosView(TemplateView):
    template_name = 'contactos.html'

class QuemSomosView(TemplateView):
    template_name = 'quem_somos.html'

class ParceriasView(TemplateView):
    template_name = 'parcerias.html'

def add_evaluation(request, campo_id, new_rating):
    # Retrieve the Campo instance
    campo = get_object_or_404(Campo, pk=campo_id)

    # Check if the new_rating is within the valid range (1 to 5)
    if 1 <= new_rating <= 5:
        # Update the total_rating and num_evaluations fields
        campo.total_rating = F('total_rating') + new_rating
        campo.num_evaluations = F('num_evaluations') + 1
        campo.calculate_average_rating()

        # Optionally, you can return a JSON response with the updated rating
        response_data = {'average_rating': campo.rating}
        return JsonResponse(response_data)

    # Handle invalid rating values here
    else:
        return JsonResponse({'error': 'Invalid rating value'})

def display_slots(request, campo_id, selected_date):
    campo = Campo.objects.get(id=campo_id)
    slots = get_slots(campo, selected_date)
    return render(request, 'display_slots.html', {'campo': campo, 'selected_date': selected_date, 'slots': slots})

def search_campos(request):
    # Retrieve search criteria from the request
    category_id = request.GET.get('category_id')
    localizacao_id = request.GET.get('localizacao_id')
    date = request.GET.get('date')

    selected_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").date()

    # Perform a query to get matching Campos based on the search criteria
    # (Replace this with your actual query based on your data model)
    matching_campos = Campo.objects.filter(categorie__id=category_id, location__id=localizacao_id).exclude(closed_days=selected_date).all()

    campos_data = []

    for campo in matching_campos:
        # Get slots for the current Campo and date
        slots = get_slots(campo, selected_date)

        print(f"Imagem: {campo.image.url}")

        # Append Campo information along with available slots to the campos_data list
        campos_data.append({
            'title': campo.title,
            'image': campo.image.url,
            'preco_hora': campo.preco_hora,
            'slots': slots,
        })

    return JsonResponse({'matching_campos': campos_data})
