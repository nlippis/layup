from layup import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^league/(?P<league_url>\w+)/$', views.league, name='league'),
        url(r'^league/(?P<league_url>\w+)/edit/$', views.edit_league, name='edit_league'),
        url(r'^league/(?P<league_url>\w+)/team/(?P<team_url>\w+)/$', views.team, name='team'),
        url(r'^player/(?P<player_url>\w+)/$', views.player, name='player'),
        url(r'^player/(?P<player_url>\w+)/edit/$', views.edit_player, name='edit_player'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.login_player, name='login'),
        url(r'^logout/$', views.logout_player, name='logout'),
        url(r'^create_league/$', views.create_league, name='create_league'),
        url(r'^manage/$', views.manage, name='manage'),
        url(r'^rest/v1.0/league/$', views.rest_league, name='rest_league'),
        url(r'^rest/v1.0/league/(?P<league_url>\w+)/$', views.rest_team, name='rest_team'),
        url(r'^rest/v1.0/league/(?P<league_url>\w+)/team/(?P<team_url>\w+)/$', views.rest_team_members, name='rest_team_members'),
        url(r'^rest/v1.0/player/(?P<player_url>\w+)/$', views.rest_player, name='rest_player'),
    )
