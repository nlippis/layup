Layup
=====

Django application that makes it easier for someone to run their basketball leagues.  

###Running Layup in docker

* Clone this repository
* Enter the repository
* Build the layup container, docker build -t \<username>/layup .
* Run the layup container, LAYUP=$(docker run -d -p :8000 \<username>/layup)
* Get the forwarded port number, docker inspect $LAYUP | grep HostPort
* Get the ip address of the host docker is running (usually ifconfig eth0)
* Open up a browser and navigate to \<docker host ip>:\<forwarded port number>/layup/
* You should now see the layup web app

###Using Layup

* To Register : Click register and fill out form
* To Login : Click login and fill out form
* To view your profile : Once logged in, click on Hi, \<username> and select view profile from the dropdown
* To edit your profile : Once logged in, click on Hi, \<username> and select edit profile from the dropdown.  Then fill out the form (you must re-enter a password).

###Managing Layup

* The only superuser is hardcoded in unfortunatly, so to manage Layup you must log in with the superuser credentials of username: commissioner password: commissioner
* Creating a League : Once logged in as superuser, click on Hi, layup and select Create League.  Fill out the form with the league name, and number of teams then click create.  The team names are automatically generated (some may be a bit weird).
* Editing a League : Once logged in as superuser, click on Hi, layup and select Manage Leagues.  From here choose a league.  You can change the league name and/or make the league inactive then click save.
* Autodrafting a league : Once logged in as superuser, click on Hi, layup and select Manage Leagues.  From here choose a league. Click on autodraft, which automatically drafts players who have signed up for the league into the leagues teams
* Delete a League : Once logged in as superuser, click on Hi, layup and select Manage Leagues.  From here choose a league.  Click on delete (this does not delete players associated with it)

###REST API

* To get a list of leagues \<ip address>:\<port>/layup/rest/v1.0/league/
* To get a list of teams associated with a league \<ip address>:\<port>/layup/rest/v1.0/league/\<league_name>/
* To get a list of players associated with a team that is associated with a league \<ip address>:\<port>/layup/rest/v1.0/league/\<league_name>/team/\<team_name>/
* To get a specific player \<ip address>:\<port>/layup/player/\<player_username>/
