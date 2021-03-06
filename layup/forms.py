from django import forms
from django.contrib.auth.models import User
from layup.models import League, Team, Player
from django.core.exceptions import ValidationError

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    Player Forms 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

class UserForm(forms.ModelForm):
    """
    Class that represents the user for authentication
    purposes, it is one part of the Player entitiy
    """

    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
                'username', 
                'first_name', 
                'last_name', 
                'email', 
                'password',
            )

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.has_key('password'):
            password = cleaned_data.get('password')

            if len(password) > 6:
                raise ValidationError('Password too long, must ' +
                    'be less than 6 characters')
        else:
            raise ValidationError('This field is required.')

        return cleaned_data
        
class EditUserForm(forms.ModelForm):
    """
    Class that represents the user for authentication
    purposes, it is one part of the Player entitiy
    """

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
                'first_name', 
                'last_name', 
                'email', 
            )

class PlayerForm(forms.ModelForm):
    """
    Form represnets the player part of the user
    information
    """

    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        self.fields['league'].queryset = League.objects.filter(status=True)
        self.fields['league'].required = True

    class Meta:
        model = Player
        fields = (
                'age', 
                'position', 
                'about', 
                'league',
            )

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    League Forms 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

class LeagueForm(forms.ModelForm):
    """
    Form represents the League entity
    """

    class Meta:
        model = League
        fields = ('name','status')

    def clean(self):
        cleaned_data = self.cleaned_data
        
        if cleaned_data.has_key('name'):
            name = cleaned_data.get('name')

            if '_' in name:
                raise ValidationError('Underscores are not allowed')
            if name is not name.strip():
                raise ValidationError('Leading and trailing spaces not allowed')
        else:
            raise ValidationError('League Name is required')
            
        return cleaned_data
