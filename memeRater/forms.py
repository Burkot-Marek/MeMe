from django.forms import ModelForm
from django import forms
from .models import Meme
from django.utils.translation import gettext as _


PUBLIC_OR_NOT = [
    ('agree','Tak'),
    ('not_agree', "Nie"),
]


class MemeForm(ModelForm):

    title = forms.CharField(label="Nadaj tytuł swojemu memowi*",
                            help_text="Tytuł musi być niepowtarzalny oraz \n zawierać maksymalnie 62 znaki",
                            error_messages={'unique':'Taki tytuł już jest zajęty',
                                            'max_length':'Tytuł może zawierać max. 62 znaki'})
    picture = forms.ImageField(label="Miejse na mema", help_text='Wybierz mema z twojego dysku którego chcesz dodać')
    dateOfBirth = forms.DateField(label="Data powstania konceptu mema", help_text="Jeśli jej nie znasz zostaw puste")
    public = forms.CharField(label="Czy chcesz udostępnić swojego mema dla wszystkich?",
                             widget=forms.RadioSelect(choices=PUBLIC_OR_NOT))

    def __init__(self, *args, **kwargs):
        super(MemeForm, self).__init__(*args, **kwargs)
        self.fields['description'].label ='Opisz mema!'

    class Meta:
        model = Meme
        fields = ['title', 'picture', 'dateOfBirth', 'description', 'public']
        # labels = {
        #     'title': _('Tytuł'),
        #     'picture': _("Mem"),
        #     'dateOfBirth': 'Data powstania konceptu mema',
        #     'description': 'Opis',
        # },
        # help_texts = {
        #     'picture': 'Każdy mem może zostać wysłany tylko raz!',
        # },
        # error_messages = {
        #     'picture': {
        #         'unique': 'Taki mem już jest na naszej stronie :)'
        #     },
        # }