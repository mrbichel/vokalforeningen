from django.forms.models import ModelForm
from models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        exclude = ('author', 'pub_date')
