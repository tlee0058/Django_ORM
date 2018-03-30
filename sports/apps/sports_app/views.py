from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.filter(league=10),
		"players": Player.objects.filter(location="Boston", team_name="Penguins"),
	}
	return render(request, "leagues/index.html", context)

def query(request, number):
    
	# 1. Find all baseball leagues | International Collegiate Baseball Conference, Atlantic Federation of Amateur Baseball Players
	if number == "1":
		context = {
			"leagues": League.objects.filter(sport="Baseball")
		}

	# 2. Find all womens' leagues | International Association of Womens' Basketball Players, Transamerican Womens' Football Athletics Conference
	elif number == "2":
		context = {
			"leagues": League.objects.filter(name__contains="Women")
		}

	# 3. Find all leagues where sport is any type of hockey | International Conference of Amateur Ice Hockey, Atlantic Amateur Field Hockey League, Pacific Ice Hockey Conference
	elif number == "3":
		context = {
			"leagues": League.objects.filter(sport__contains="Hockey")
		}

	# 4. Find all leagues where sport is something OTHER THAN football | International Conference of Amateur Ice Hockey, International Collegiate Baseball Conference, Atlantic Federation of Amateur Baseball Players, Atlantic Federation of Basketball Athletics, Atlantic Soccer Conference, International Association of Womens' Basketball Players, Atlantic Amateur Field Hockey League, Pacific Ice Hockey Conference
	elif number == "4":
		context = {
			"leagues": League.objects.exclude(sport="Football")
		}

	# 5. Find all leagues that call themselves "conferences" | International Conference of Amateur Ice Hockey, International Collegiate Baseball Conference, Atlantic Soccer Conference, American Conference of Amateur Football, Transamerican Womens' Football Athletics Conference, Pacific Ice Hockey Conference
	elif number == "5":
		context = {
			"leagues": League.objects.filter(name__contains="Conference")
		}

	# 6. Find all leagues in the Atlantic region | Atlantic Federation of Amateur Baseball Players, Atlantic Federation of Basketball Athletics, Atlantic Soccer Conference, Atlantic Amateur Field Hockey League
	elif number == "6":
		context = {
			"leagues": League.objects.filter(name__startswith="Atlantic")
		}

	# 7. Find all teams based in Dallas | Dallas Nets, Dallas Angels
	elif number == "7":
		context = {
			"teams": Team.objects.filter(location="Dallas")
		}

	# 8. Find all teams named the Raptors | Atlanta Raptors, Golden State Raptors
	elif number == "8":
		context = {
			"teams": Team.objects.filter(team_name__contains="Raptors")
		}

	# 9. Find all teams whose location includes "City" | Mexico City Cave Spiders, Kansas City Spurs
	elif number == "9":
		context = {
			"teams": Team.objects.filter(location__contains="City")
		}

	# 10. Find all teams whose names begin with "T" | Alberta Texans, Michigan Timberwolves, Manitoba Tiger-Cats, Colorado Twins
	elif number == "10":
		context = {
			"teams": Team.objects.filter(team_name__startswith="T")
		}

	# 11. Return all teams, ordered alphabetically by location | *too many to list*
	elif number == "11":
		context = {
			"teams": Team.objects.order_by('location')
		}

	# 12. Return all teams, ordered by team name in reverse alphabetical order | *too many to list*
	elif number == "12":
		context = {
			"teams": Team.objects.order_by('-team_name')
		}

	# 13. Find every player with last name "Cooper" | Joshua Cooper, Landon Cooper, Michael Cooper, Alexander Cooper
	elif number == "13":
		context = {
			"players": Player.objects.filter(last_name="Cooper")
		}

	# 14. Find every player with first name "Joshua" | Joshua Cooper, Joshua Hayes, Joshua Henderson, Joshua Long, Joshua Coleman, Joshua White, Joshua Parker, Joshua Smith
	elif number == "14":
		context = {
			"players": Player.objects.filter(first_name="Joshua")
		}

	# 15. Find every player with last name "Cooper" EXCEPT FOR Joshua | Landon Cooper, Michael Cooper, Alexander Cooper
	elif number == "15":
		context = {
			"players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
		}

	# 16. Find all players with first name "Alexander" OR first name "Wyatt" | Wyatt Bell, Alexander Bailey, Wyatt Peterson, Alexander Wright, Wyatt Alexander, Wyatt Bennett, Alexander Parker, Alexander Adams, Alexander Walker, Alexander Flores, Alexander Cooper
	elif number == "16":
		context = {
			# "players": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt")
			"players": Player.objects.filter(first_name__in=["Alexander","Wyatt"])
		}

	return render(request, "leagues/index.html", context)


# ********************************** Optional Assignment: Sports ORM II **************************************
# This is the second part of the Sports ORM assignment. Note that, in the models, every player has exactly one .curr_team, and every team has exactly one .league. 
# ForeignKey Relationships

def queryII(request, number):

	# 1. Find all teams in the Atlantic Soccer Conference | Minneapolis Wizards, Pittsburgh Bruins, Cleveland Dolphins, Toronto Pirates, Golden State Raptors
	if number == "1":
		context = {
			"teams": Team.objects.filter(league__name='Atlantic Soccer Conference')
		}

	# 2. Find all (current) players on the Boston Penguins | Landon Hernandez, Wyatt Bennett, David Sanchez
	if number == "2":
		context = {
			"players": Player.objects.filter(curr_team__team_name="Penguins", curr_team__location="Boston")
		}

	# 3. Find all (current) players in the International Collegiate Baseball Conference | Michael Flores, Abigail Foster, Ryan Phillips, Elijah Powell, Isaac Perry, Charlotte Jones, Sophia Rivera, Isabella Griffin, Landon Cooper, Elijah James, Abigail Davis, Wyatt Alexander, Abigail Richardson, Jacob Jenkins, Landon Gray, Levi Miller, Joshua Long, Nathan Mitchell, James Ramirez, Samuel Evans, John Edwards, Henry Martin, Andrew Adams, Joshua White, Alexander Flores, Abigail Hernandez, Caleb Parker, Joshua Smith, Jack Phillips
	if number == "3":
		context = {
			"players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference")
		}

	# 4. Find all (current) players in the American Conference of Amateur Football with last name "Lopez" | Levi Lopez, Isabella Lopez	
	if number == "4":
		context = {
			"players": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football").filter(last_name="Lopez")
		}

	# 5. Find all football players | Nathan Bryant, Wyatt Bell, Lucas Martin, Luke Lopez, Dylan Rodriguez, Luke Bell, James Ross, Benjamin King, Caleb Martinez, Jack Young, Anthony Martinez, Jaxon Gonzales, Emily Sanchez, Jaxon Torres, Liam Watson, James Smith, Dylan Garcia, Joshua Cooper, Aiden Rivera, Benjamin Alexander, Ava Henderson, Joshua Hayes, Landon Mitchell, Charles Collins, Nathan Brooks, Isabella Bennett, Lucas Perry, Charles Campbell, Alexander Parker, Benjamin Perry, Levi Lopez, Charlotte Ross, Oliver Kelly, Daniel Martinez, Ryan Peterson, Isabella Lopez, Charlotte Harris, Caleb Collins, Ryan Gonzales, Joseph Roberts, David Watson, Abigail Long, Landon James, Daniel Davis, Charlotte Brown, Logan King, Luke Clark, Isabella Lewis, Jacob Gray, Liam Robinson, Aiden Hernandez, Christian Wood, Joshua Parker, Ethan Sanchez, Noah Brooks, Charles Campbell, Mason Henderson, Nathan Flores, Jackson Perry, Noah Taylor, Levi Howard, Jayden Perez, Elijah Richardson, Emily Jackson, Olivia Young, Abigail Torres, Christopher Sanders
	if number == "5":
		context = {
			"players": Player.objects.filter(curr_team__league__sport="Football")
		}

	# 6. Find all teams with a (current) player named "Sophia" | Mexico City Cave Spiders, Houston Hornets, Wisconsin Devils
	if number == "6":
		context = {
			"teams": Team.objects.filter(curr_players__first_name="Sophia")
		}

	# 7. Find all leagues with a (current) player named "Sophia" | International Collegiate Baseball Conference, Atlantic Federation of Basketball Athletics, Atlantic Amateur Field Hockey League
	if number == "7":
		context = {
			"leagues": League.objects.filter(teams__curr_players__first_name="Sophia")
		}

	# 8. Find everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders | Michael Flores, Alexander Flores, Nathan Flores
	if number == "8":
		context = {
			# "players":Player.objects.exclude(curr_team__team_name="Roughriders").filter(last_name="Flores") | Player.objects.exclude(curr_team__location="Washington").filter(last_name="Flores")
			"players":Player.objects.exclude(curr_team__team_name="Roughriders", curr_team__location="Washington").filter(last_name="Flores")
		}

	return render(request, "leagues/index.html", context)

	# ManyToMany Relationships

def queryIII(request, number):

	# 1. Find all teams, past and present, that Samuel Evans has played with | Dallas Nets, Montreal White Sox, Ohio Black Sox, Indianapolis Athletics, Mexico City Cave Spiders, Ontario Outlaws
	if number == "1":
		context = {
			"teams": Team.objects.filter(all_players__first_name="Samuel") &  Team.objects.filter(all_players__last_name="Evans") 
		}

	# 2. Find all players, past and present, with the Manitoba Tiger-Cats | Jaxon Howard, Sophia Bailey, Alexander Bailey, Levi Rodriguez, William Martin, Olivia Diaz, Jacob Green, Christian Perez, Harper James, Daniel Kelly
	if number == "2":
		context = {
			"players": Player.objects.filter(all_teams__team_name="Tiger-Cats") &  Player.objects.filter(all_teams__location="Manitoba") 
		}

	# 3. Find all players who were formerly (but aren't currently) with the Wichita Vikings | Dylan Rodriguez, Aiden Rivera, Ava Henderson, Nathan Brooks, Daniel Martinez, Ryan Peterson, Charlotte Harris, Noah Brooks, Levi Howard, Christopher Sanders
	if number == "3":
		context = {
			# "players": Player.objects.filter(all_teams__team_name="Vikings").exclude(curr_team__team_name="Vikings") &  Player.objects.filter(all_teams__location="Wichita").exclude(curr_team__location="Wichita")
			"players": Player.objects.filter(all_teams__team_name="Vikings").exclude(curr_team__team_name="Vikings").filter(all_teams__location="Wichita").exclude(curr_team__location="Wichita")
		}

	# 4. Find every team that Jacob Gray played for before he joined the Oregon Colts | Puerto Rico Breakers, Toronto Kings, Ontario Gunslingers
	if number == "4":

		context = {
			"teams": Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(curr_players__first_name="Jacob", curr_players__last_name="Gray"),

		}
	# 5. Find everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players | Joshua Long, Joshua White, Joshua Smith
	if number == "5":
		
		context = {
			"players": Player.objects.filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players").filter(first_name="Joshua")
		}

	# 6. Find all teams that have had 12 or more players, past and present.  (HINT: Look up the Django `annotate` function.) | Dallas Nets, California Padres, Montreal White Sox, Alberta Texans, Puerto Rico Breakers, South Carolina Wolverines, Washington Roughriders, Edmonton Warriors, Toronto Kings, Wisconsin Rams, Michigan Timberwolves, Phoenix Rays, Ontario Gunslingers, Texas Diamondbacks, Oregon Colts, Mexico City Cave Spiders, Raleigh Bulls, Montreal Wild, Wisconsin Devils, Indiana Royals, Maryland Cowboys, Ontario Outlaws, Dallas Angels, Kansas City Spurs
	if number == "6":
		context = {
			"teams": Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12)
		}

	# 7. Show all players, sorted by the number of teams they've played for | *too many to list, but the first few are Olivia Rodriguez, Ryan Phillips, and Luke Bell*
	if number == "7":
		context = {
			"players": Player.objects.annotate(num_teams=Count('all_teams')).order_by('num_teams')
		}

	return render(request, "leagues/index.html", context)



def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")