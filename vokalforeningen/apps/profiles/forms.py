# -*- coding: utf-8 -*-

"""
Forms and validation code for user registration.

"""
from __future__ import unicode_literals

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
from models import Profile

# I put this on all required fields, because it's easier to pick up
# on them with CSSf or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = {'class': 'required'}

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label=_("Email"))


class RegistrationForm(forms.Form):
    """
    Form for registering a new user account.
    """

    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("E-mail"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_("Password (again)"))

    first_name = forms.CharField(max_length=140, label="Fornavn")
    last_name = forms.CharField(max_length=140, label="Efternavn")

    address = forms.CharField(max_length=255, widget=forms.Textarea(), label='Adresse')
    mobile_phone_number = forms.CharField(max_length=12, label='Mobil')
    postal_code = forms.CharField(max_length=5, label='Postnummer')
    city = forms.CharField(max_length=255, label='By')
    
    accept = forms.BooleanField(label='Accepter vedtægter og modtagelse af nyhedsbrev')


    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']
    
    def clean_accept(self):
        """
        """
        
        if self.cleaned_data['accept'] is False:
            raise forms.ValidationError("Du skal accepterer Dansk Vokalforenings vedtægter og modtagelse af vores nyhedsbrev.")
        
        return self.cleaned_data['accept']
    
    
    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
                
        return self.cleaned_data


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('url',
                  'address',
                  'postal_code',
                  'city',
                  'phone_number',
                  'birthdate',
                  'bio',
                  'image',
                  'receive_email',
                  'facebook',
            )

#class EmailInactiveUsers(forms.Form):
#    title =
