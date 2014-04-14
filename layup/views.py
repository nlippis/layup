from django.contrib.auth.models import User
from layup.models import League, Team, Player
from layup.forms import UserForm, PlayerForm
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
              Url Decoding Functions 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

def decode_url(item):
     return  item.replace('_',' ')

def encode_url(item):
     return  item.replace(' ','_')

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                    Page Views 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

def index(request):
    """
    Index page view, displaying all active leagues
    """

    active_leagues = League.objects.filter(status=True)

    # Replace spaces with underscores for url representation
    for league in active_leagues:
        league.url = encode_url(league.name)

    context = {'leagues' : active_leagues}

    return render(request, 'layup/index.html', context)

def league(request, league_url):
    """
    League page view, displaying all teams in specified
    league
    """
    
    # Check for valid league
    league_name = decode_url(league_url)
    league = get_object_or_404(League, name=league_name)

    teams = league.team_set.all()

    for team in teams:
        team.url = encode_url(team.name)

    context = {
            'league': league.name,
            'teams': teams,
        }

    return render(request, 'layup/league.html', context)

def team(request, team_url):
    """
    Team page view, displaying all players in specified
    team
    """

    # Check for valid team 
    team_name = decode_url(team_url)
    team = get_object_or_404(Team, name=team_name)

    players = team.player_set.all()

    for player in players:
        player.url = encode_url(player.user.username)

    context = {
            'team': team.name,
            'players': players,
        }

    return render(request, 'layup/team.html', context)

def player(request, player_url):
    """
    Player page view, displaying the characteristics
    of the player
    """

    # Check for valid player
    player_name = decode_url(player_url)
    user = get_object_or_404(User, username=player_name)
    player = get_object_or_404(Player, user=user)

    # Filter values, so only relevant data shown

    context = {'player': player}

    return render(request, 'layup/player.html', context)

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
               Login/Registration Views 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

def register(request):
    """
    Registration page view
    """

    registered = False

    # If form submitted
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        player_form = PlayerForm(data=request.POST)

        # Validate forms
        if user_form.is_valid() and player_form.is_valid():
            # Process user form data
            user = user_form.save()
            
            # Hash password and insert user into db
            user.set_password(user.password)
            user.save()

            # Process player form data
            player = player_form.save(commit=False)

            # Create relation from player to user
            # and insert player into db
            player.user = user
            player.save()

            registered = True

        # If mistakes in form
        else:
            print user_form.errors, player_form.errors

    # Accessing register page for first time
    else:
        user_form = UserForm()
        player_form = PlayerForm()

    # Create context dict for page rendering
    context = {
            'user_form': user_form,
            'player_form': player_form,
            'registered': registered,
        }

    return render(request, 'layup/register.html', context)

def player_login(request):
    """
    Player Login page view
    """

    # If form submitted
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # If authentication successful
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/layup/')
        else:
            return HttpResponse("Invalid login details supplied.")

    # Accessing login page for first time
    else:
        return render(request, 'layup/login.html', {})

@login_required
def player_logout(request):
    """
    Player logout redirect
    """

    logout(request)

    # Return user back to homepage
    return HttpResponseRedirect('/layup/')
