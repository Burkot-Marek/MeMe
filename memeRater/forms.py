from django.forms import ModelForm
from .models import Meme


class MemeForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MemeForm, self).__init__(*args, **kwargs)
        self.fields['title'].label ='TYTUŁ TUTAJ ZJEBIE'

    class Meta:
        model = Meme
        fields = ['title', 'picture', 'dateOfBirth', 'description']
        labels = {
            'title': 'Tytuł',
            'picture': "Mem",
            'dateOfBirth': 'Data powstania konceptu mema',
            'description': 'Opis',
        },
        help_texts = {
            'picture': 'Każdy mem może zostać wysłany tylko raz!',
        },
        error_messages = {
            'picture': {
                'unique': 'Taki mem już jest na naszej stronie :)'
            },
        }