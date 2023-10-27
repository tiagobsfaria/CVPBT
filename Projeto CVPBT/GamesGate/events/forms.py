from django import forms
from .models import Campo, Categorie


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ('title', 'category_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CampoCreateForm(forms.ModelForm):
    class Meta:
        model = Campo
        fields = ('title', 'localizacao', 'content', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

