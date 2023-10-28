from django import forms
from .models import Campo, Categorie, Localizacao


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ('title',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
                    'title': 'Título',  # Change the label for the 'title' field
                }

class CampoForm(forms.ModelForm):
    localizacao = forms.ModelChoiceField(
        queryset=Localizacao.objects.all(),  # Provide a queryset to populate the dropdown
        empty_label="Select a Localizacao",  # Optional: Add an empty label for better user experience
        widget=forms.Select(attrs={'class': 'form-control'})  # Apply class to the dropdown
    )

    class Meta:
        model = Campo
        fields = ('title', 'location', 'content', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

