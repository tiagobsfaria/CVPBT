from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.
class home(TemplateView):
    template_name = 'home.html'

class CategorieListView(ListView):
    model = Categorie
    template_name = "categories_list.html"


def CategorieView(request, cats):
    return render(request, 'campo.html', {"cats":cats})

class CategorieCreateView(CreateView):
    model = Categorie
    template_name = "categorie_create.html"
    form_class = CategorieForm
    success_url = reverse_lazy("list-categories")

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "categorie_delete.html"

    success_url = reverse_lazy("list-categories")

class CategorieEditView(UpdateView):
    model = Categorie
    template_name = "categorie_edit.html"
    form_class = CategorieForm
    success_url = reverse_lazy("list-categories")

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "categorie_detail.html"


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