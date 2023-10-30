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

class AvailableSlotsField(forms.MultiValueField):
    widget = forms.TextInput(attrs={'placeholder': 'Enter available slots by weekday and specify closed days'})

    def __init__(self, *args, **kwargs):
        fields = [
            forms.CharField(),
            forms.BooleanField(required=False),
        ]
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        slots = []
        for i in range(0, len(data_list), 2):
            weekday = data_list[i]
            is_closed = data_list[i + 1]
            if not is_closed:
                slots.append(f"{weekday}: {data_list[i + 2]}-{data_list[i + 3]}")
        return slots

class CampoForm(forms.ModelForm):
    WEEKDAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    title = forms.CharField(max_length=200)
    location = forms.ModelChoiceField(
        queryset=Localizacao.objects.all(),
        empty_label="Select a Localizacao",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    content = forms.Textarea(attrs={'class': 'form-control'})
    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    available_slots = AvailableSlotsField(required=False)

    class Meta:
        model = Campo
        fields = ('title', 'location', 'content', 'categorie', 'available_slots')

        labels = {
            'title': 'Título',
            'location': 'Localização',
        }
