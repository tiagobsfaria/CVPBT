from django import forms
from .models import Campo, Categorie, Localizacao
from django.contrib.auth.models import User


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

class AvailableSlotsField(forms.MultiValueField):
    widget = forms.TextInput(attrs={'placeholder': 'Enter available slots by weekday and specify closed days'})

    def __init__(self, *args, **kwargs):
        fields = [
            forms.CharField(),
            forms.BooleanField(required=False),
            forms.TimeField(),
            forms.TimeField(),
        ]
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        slots = []
        for i in range(0, len(data_list), 4):
            weekday = data_list[i]
            is_closed = data_list[i + 1]
            if not is_closed:
                opening_time = data_list[i + 2]
                closing_time = data_list[i + 3]
                slots.append(f"{weekday}: {opening_time}-{closing_time}")
        return slots

class CampoForm(forms.ModelForm):
    class Meta:
        model = Campo
        fields = ['title', 'location', 'content', 'categorie', 'author', 'likes', 'rating', 'num_evaluations',
                  'monday_opening', 'monday_closing', 'tuesday_opening', 'tuesday_closing',
                  'wednesday_opening', 'wednesday_closing', 'thursday_opening', 'thursday_closing',
                  'friday_opening', 'friday_closing', 'saturday_opening', 'saturday_closing',
                  'sunday_opening', 'sunday_closing', 'closed_days', 'image']

    title = forms.CharField(max_length=200)
    location = forms.ModelChoiceField(queryset=Localizacao.objects.all())
    content = forms.Textarea()
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all())
    author = forms.ModelChoiceField(queryset=User.objects.all())
    likes = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    rating = forms.IntegerField()
    num_evaluations = forms.IntegerField()
    monday_opening = forms.TimeField()
    monday_closing = forms.TimeField()
    tuesday_opening = forms.TimeField()
    tuesday_closing = forms.TimeField()
    wednesday_opening = forms.TimeField()
    wednesday_closing = forms.TimeField()
    thursday_opening = forms.TimeField()
    thursday_closing = forms.TimeField()
    friday_opening = forms.TimeField()
    friday_closing = forms.TimeField()
    saturday_opening = forms.TimeField()
    saturday_closing = forms.TimeField()
    sunday_opening = forms.TimeField()
    sunday_closing = forms.TimeField()
    closed_days = forms.DateField()
    image = forms.ClearableFileInput(attrs={'multiple': False})
