from layup.forms import LeagueForm 
from django.core import serializers
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from layup.models import League, Team, Player
from layup.serializers import league_serializer
from layup.team_namer import team_name_generator
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from layup.forms import UserForm, PlayerForm, EditUserForm
from django.contrib.auth.decorators import user_passes_test


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

    # Set url value for team redirect
    league.url = league_url
    
    teams = league.team_set.all()

    for team in teams:
        team.url = encode_url(team.name)

    context = {
            'league': league,
            'teams': teams,
        }

    return render(request, 'layup/league.html', context)

def team(request, league_url, team_url):
    """
    Team page view, displaying all players in specified
    team
    """

    # Check for valid league / team 
    league_name = decode_url(league_url)
    league = get_object_or_404(League, name=league_name)

    team_name = decode_url(team_url)
    team = get_object_or_404(league.team_set, name=team_name)

    players = team.player_set.all()

    context = {
            'league': league,
            'team': team,
            'players': players,
        }

    return render(request, 'layup/team.html', context)

def player(request, player_url):
    """
    Player page view, displaying the characteristics
    of the player
    """

    # Check for valid player
    user = get_object_or_404(User, username=player_url)
    player = get_object_or_404(Player, user=user)

    context = {'player': player}

    return render(request, 'layup/player.html', context)

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                      REST API 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

def rest_league(request):
    """
    REST view for league, returns all league names
    """

    try:
        active_leagues = League.objects.filter(status=True)
        serializer = league_serializer()
        data = serializer.serialize(active_leagues)
    except:
        data = None

    return HttpResponse([data], mimetype='application/json')

def rest_team(request, league_url):
    """
    REST view for team, returns all team names, associated
    with league
    """

    # Check for valid league 
    league_name = decode_url(league_url)

    try:
        league = League.objects.get(name=league_name)
        league_teams = league.team_set.all()
        serializer = league_serializer()
        data = serializer.serialize(league_teams, fields=('name',))
    except:
        data = None

    return HttpResponse([data], mimetype='application/json')

def rest_team_members(request, league_url, team_url):
    """
    Rest for for team members, returns all player names,
    associated with team
    """

    # Check for valid data 
    try:
        league_name = decode_url(league_url)
        league = League.objects.get(name=league_name)

        team_name = decode_url(team_url)
        team = league.team_set.get(name=team_name)

        players = team.player_set.all()

        data = []
        for player in players:
            data.append(extract_player(player.user))
    except:
        data = None

    return HttpResponse(data, mimetype='application/json')

def rest_player(request, player_url):
    """
    Player page view, displaying the characteristics
    of the player
    """

    # Check for valid player
    try:
        user = User.objects.get(username=player_url)
        data = extract_player(user)
    except:
        data = None

    return HttpResponse(data, mimetype='application/json')

def extract_player(user):
    """
    HELPER FUNCTION
    Due to "player" being a dual entity object, data from 
    the User model and Player moded needs to be merged
    so that this architectural detail is abstracted from
    the user
    """

    player = Player.objects.get(user=user)

    serializer = league_serializer()
    user_data = serializer.serialize(
            [user], 
            fields=(
                'username',
                'first_name',
                'last_name',
                'email'
                )
        )
    player_data = serializer.serialize(
            [player], 
            fields=(
                'age',
                'position',
                'team',
                'league',
                'about'
                )
        )

    # Merge datasets
    user_data[0].update(player_data[0])

    # Swap pk's for league and team for names
    try:
        user_data[0]['league'] = player.league.name
        user_data[0]['team'] = player.team.name
    except:
        pass

    return user_data

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                   Data Edit Views 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

@user_passes_test(lambda u: u.is_superuser)
def create_league(request):
    """
    Create new league view
    """

    # If form submitted
    if request.method =='POST':
        league_form = LeagueForm(request.POST)

        if league_form.is_valid():
            # Process user update
            league = league_form.save()
            league.save()

            # Get number of teams to create
            num_teams = int(request.POST['teams'])

            for team in xrange(num_teams):
                team_name = team_name_generator()
                league.team_set.create(name=team_name)
            
            return HttpResponseRedirect(
                    '/layup/league/%s/' % encode_url(league.name) 
                )

    # Accessing create league page for first time
    else:
        league_form = LeagueForm()

    # Create context dict for page rendering
    context = {
            'league_form': league_form,
            'player': player,
        }

    return render(request, 'layup/create_league.html', context)

@user_passes_test(lambda u: u.is_superuser)
def edit_league(request, league_url):
    """
    Edit league view
    """
    
    league_name = decode_url(league_url)
    league = get_object_or_404(League, name=league_name)

    league.url = encode_url(league.name)
    
    # If form submitted
    if request.method == 'POST':

        # Delete League
        if request.POST.has_key('delete'):
            league.delete()

        # Autodraft players in to league
        elif request.POST.has_key('autodraft'):
            # Get unassigned players an all teams
            players = Player.objects.filter(league=league, team=None)
            teams = league.team_set.all()
            
            # Assign all unassigned players to a team
            num_teams = teams.count()
             
            if num_teams > 0:
                team_index = 0
                for player in players:
                    if team_index >= num_teams:
                        team_index = 0
                    player.team = teams[team_index]
                    player.save()
                    team_index += 1

        # Update League with new information
        else:
            league_form = LeagueForm(request.POST, instance=league)

            if league_form.is_valid():
                # Process user update
                league = league_form.save()
                league.save()

        return HttpResponseRedirect('/layup/manage/')

    # Accessing create league page for first time
    else:
        league_form = LeagueForm(instance=league)

    # Create context dict for page rendering
    context = {
            'league_form': league_form,
            'league': league,
        }

    return render(request, 'layup/edit_league.html', context)

@login_required
def edit_player(request, player_url):
    """
    Player edit profile view
    """
    
    #Check for valid player
    user = get_object_or_404(User, username=player_url)
    player = get_object_or_404(Player, user=user)

    # If form submitted
    if request.method =='POST':
        user_form = EditUserForm(request.POST, instance=user)
        player_form = PlayerForm(request.POST, instance=player)

        if user_form.is_valid() and player_form.is_valid():
            # Process user update
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # Process player form data
            player = player_form.save()
            player.save()

            return HttpResponseRedirect(
                    '/layup/player/%s/' % player_url
                )

    # Accessing register page for first time
    else:
        user_form = EditUserForm(instance=user)
        player_form = PlayerForm(instance=player)

    # Create context dict for page rendering
    context = {
            'user_form': user_form,
            'player_form': player_form,
            'player': player,
        }

    return render(request, 'layup/edit_player.html', context)

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

def login_player(request):
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
def logout_player(request):
    """
    Player logout redirect
    """

    logout(request)

    # Return user back to homepage
    return HttpResponseRedirect('/layup/')

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
          Management Pages COMISSIONER ONLY 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

@user_passes_test(lambda u: u.is_superuser)
def manage(request):
    """
    Management page; create or edit leagues
    """

    leagues = League.objects.all()

    # Replace spaces with underscores for url representation
    for league in leagues:
        league.url = encode_url(league.name)

    context = {'leagues' : leagues}

    return render(request, 'layup/manage.html', context)
