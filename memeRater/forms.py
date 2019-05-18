from django.forms import ModelForm
from django import forms
from .models import Meme


PUBLIC_OR_NOT = [
    ('True','Tak'),
    ('False', "Nie"),
]
helpValue = "Jeśli nie znasz, zostaw pole puste."


class AddForm(ModelForm):
    title = forms.CharField(label="Nadaj tytuł swojemu memowi*",
                            help_text="Tytuł musi być niepowtarzalny oraz \n zawierać maksymalnie 62 znaki",
                            error_messages={'unique': 'Taki tytuł już jest zajęty',
                                            'max_length':'Tytuł może zawierać max. 62 znaki'})
    picture = forms.ImageField(label="Miejse na mema*", help_text='Pokaż nam tego świetnego mema!')
    dateOfBirth = forms.DateField(label="Data powstania konceptu mema",                                                         #dodać kalendarz do pół typu DateField
                                  help_text=helpValue,
                                  required=False)
                                #error_messages={'valueError':                   "Wpisz poprawną datę w formacie YY-MM-DD"})   dodać tutaj inny error message, sprawdzić jaki to error
    public = forms.CharField(label= "Czy chcesz udostępnić swojego mema dla wszystkich?*",
                             help_text= "Jeśli wybierzesz nie, tylko ty będziesz miał do nich dostęp :(",
                             widget=forms.RadioSelect(choices=PUBLIC_OR_NOT))

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['description'].label ='Opisz mema!*'
        self.fields['description'].help_text="Pomóź nam w opisie swojego mema"

    class Meta:
        model = Meme
        fields = ['title', 'picture', 'dateOfBirth', 'description', 'public']


class EditForm(ModelForm):
    title = forms.CharField(label="Tytuł opisujący mema*",
                            help_text="Pamiętaj by stworzyć unikalny tytułm zawierający do 62 znaków")
    dateOfBirth = forms.DateField(label="Data powstania konceptu mema",
                                  help_text=helpValue,
                                  required=False)
    dateOfDeath = forms.DateField(label='Data tzw. "śmierci" mema',
                                  help_text=helpValue,
                                  required=False)
    public = forms.CharField(label= "Czy chcesz udostępnić swojego mema dla wszystkich?*",
                             help_text= "Jeśli wybierzesz nie, tylko ty będziesz miał do nich dostęp :(",
                             widget=forms.RadioSelect(choices=PUBLIC_OR_NOT))

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['description'].label ='Opis*'
        self.fields['description'].help_text="Tutaj możesz zmienić opis swojego mema"

    class Meta:
        model = Meme
        exclude = ['picture', 'memeClass']