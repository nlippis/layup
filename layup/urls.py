from layup import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^league/(?P<league_url>\w+)/$', views.league, name='league'),
        url(r'^league/(?P<league_url>\w+)/team/(?P<team_url>\w+)/$', views.team, name='team'),
        url(r'^player/(?P<player_url>\w+)/$', views.player, name='player'),
        url(r'^player/(?P<player_url>\w+)/edit/$', views.player_edit, name='player_edit'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.player_login, name='login'),
        url(r'^logout/$', views.player_logout, name='logout'),
    )
