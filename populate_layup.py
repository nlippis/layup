import os

def populate():
    ne_league = add_league('New England')

    celtics = add_team(
            league=ne_league,
            name="Celtics"
        )

    add_player(
            username='a',
            email='a@layup.com',
            password='a',
            league=ne_league,
            team=celtics,
            age=23,
            position='C'
        )

    mariners = add_team(
            league=ne_league,
            name="Mariners"
        )

    add_player(
            username='b',
            email='a@layup.com',
            password='a',
            league=ne_league,
            team=mariners,
            age=24,
            position='F'
        )

    lobstermen = add_team(
            league=ne_league,
            name="Lobstermen"
        )

    add_player(
            username='c',
            email='c@layup.com',
            password='c',
            league=ne_league,
            team=lobstermen,
            age=25,
            position='G'
        )

    nc_league = add_league('North California')

    redwoods = add_team(
            league=nc_league,
            name="Redwoods"
        )

    add_player(
            username='d',
            email='d@layup.com',
            password='d',
            league=nc_league,
            team=redwoods,
            age=26,
            position='C'
        )

    baymen = add_team(
            league=nc_league,
            name="Baymen"
        )

    add_player(
            username='e',
            email='e@layup.com',
            password='e',
            league=nc_league,
            team=baymen,
            age=27,
            position='F'
        )

    warriors = add_team(
            league=nc_league,
            name="Warriors"
        )

    add_player(
            username='f',
            email='f@layup.com',
            password='f',
            league=nc_league,
            team=warriors,
            age=28,
            position='G'
        )

    ny_league = add_league('New York')

    nets = add_team(
            league=ny_league,
            name="Nets"
        )

    add_player(
            username='g',
            email='g@layup.com',
            password='g',
            league=ny_league,
            team=nets,
            age=29,
            position='C'
        )

    forgetaboutits = add_team(
            league=ny_league,
            name="Forgetaboutits"
        )

    add_player(
            username='h',
            email='h@layup.com',
            password='h',
            league=ny_league,
            team=forgetaboutits,
            age=30,
            position='F'
        )

    empires = add_team(
            league=ny_league,
            name="Empires"
        )

    add_player(
            username='i',
            email='i@layup.com',
            password='i',
            league=ny_league,
            team=empires,
            age=31,
            position='G'
        )

    # Print out what we have added to the user
    for l in League.objects.all():
        for t in Team.objects.filter(league=l):
            for p in Player.objects.filter(team=t):
                print "- {0} - {1} - {2}".format(str(l), str(t), str(p))

def add_league(name):
    l = League.objects.get_or_create(name=name)[0]
    return l 

def add_team(league, name):
    t = Team.objects.get_or_create(league=league, name=name)[0]
    return t 

def add_player(username, email, password, league, team, age, position):
    # Create User object
    u = User.objects.get_or_create(
            username=username,
            password=password,
            email=email,
        )[0]

    # Create Player object
    p = Player.objects.get_or_create(
            user=u,
            league=league,
            team=team,
            age=age,
            position=position,
        )[0]

    return u, p

# Start execution here!
if __name__ == '__main__':
    print "Staring Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'layup_project.settings')
    from django.contrib.auth.models import User
    from layup.models import League, Team, Player
    populate()
