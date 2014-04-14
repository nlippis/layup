from django import forms
from django.contrib.auth.models import User
from layup.models import League, Team, Player

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
                'password',
            )

class PlayerForm(forms.ModelForm):
    """
    Form represnets the player part of the user
    information
    """

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
        fields = ('name',)

class EditLeagueForm(forms.ModelForm):
    """
    Form used for editing the League entity
    """

    class Meta:
        model = League
        fields = ('status',)
