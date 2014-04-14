from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                       Models
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

class League(models.Model):
    """
    Represents a league, associated with many teams and 
    many players
    """
    
    name = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class Team(models.Model):
    """
    Represents a team, associated with one league and 
    many players
    """

    # Relations
    league = models.ForeignKey(League)

    # Player specific fields
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Player(models.Model):
    """
    Represents a player, associated with one league and 
    one team.  In addition extends the User class for
    direct coupling to django's authentication system
    """

    # Relations
    user = models.OneToOneField(User) 

    league = models.ForeignKey(
            League,
            blank=True,
            null=True,
            on_delete=models.SET_NULL
        )

    team = models.ForeignKey(
            Team,
            blank=True,
            null=True,
            on_delete=models.SET_NULL
        )


    # Player specific fields
    one_hundred_limit = MaxValueValidator(100)

    age = models.PositiveSmallIntegerField(
            validators=[one_hundred_limit],
        )
    
    position_choices = (
            ('C', 'Center'),
            ('F', 'Forward'),
            ('G', 'Guard'),
        )

    position = models.CharField(
            max_length=1,
            choices=position_choices,
        )

    about = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.username
