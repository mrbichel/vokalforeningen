from django.forms.models import ModelForm, BaseForm
from django import forms
from django.forms.fields import DateField, TimeField
from models import Note


class TimeForm(forms.Form):
    start_date = DateField()
    start_time = TimeField()
    end_date = DateField()
    end_time = TimeField()

    #def clean(self):

class NoteForm(ModelForm):
    class Meta:
        model = Note
        exclude = ('author', 'pub_date', 'start', 'end')

