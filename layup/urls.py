from layup import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^league/(?P<league_url>\w+)/$', views.league, name='league'),
        url(r'^league/(?P<league_url>\w+)/team/(?P<team_url>\w+)/$', views.team, name='team'),
        url(r'^player/(?P<player_url>\w+)/$', views.player, name='player'),
        url(r'^player/(?P<player_url>\w+)/edit/$', views.edit_player, name='edit_player'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.login_player, name='login'),
        url(r'^logout/$', views.logout_player, name='logout'),
    )
