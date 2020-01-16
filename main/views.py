# Modules needed for this to work:
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users, statistics, removeMe, mediaFiles
from background_task import background

import requests
import datetime
import time

# API variables

id_client = 34525
secret_client = "ab4bd218533ac10f2527b321ea4c01dce1cfb664"

# Change access_token if old
def refreshToken(refresh_tokens, athlete_id):
	r = requests.post(url = "https://www.strava.com/oauth/token", params = {"client_id" : id_client, "client_secret" : secret_client, "refresh_token" : refresh_tokens, "grant_type" : "refresh_token"})
	data = r.json()
	print(data)


	expires_at = data["expires_at"]
	access_token = data["access_token"]

	user = Users.objects.get(ied=athlete_id)
	user.expires_at = expires_at
	user.access_token = access_token
	user.save()

	print("Changed %s 's access_token to %s" % (user.firstName, user.access_token))

# Refresh athletes data and check wether access_token is expired
def refreshData(refresh):
	for user in Users.objects.all():
		if user.expires_at - time.time() < 0:
			print("Creating new access_token and refreshing data for ", user.firstName)
			refreshToken(user.refresh_token, user.ied)

	if refresh:
		for user in Users.objects.all():
			print(user.access_token)

			stats = statistics.objects.get(ied=user.ied)
			r = requests.get("https://www.strava.com/api/v3/athletes/" + user.ied + "/stats?access_token=" + user.access_token + "&per_page=1000")
			data = r.json()

			try:
				ride = data["all_ride_totals"]
				y = data["ytd_ride_totals"]
				b = data["recent_ride_totals"]

				stats.biggest_ride_distance=data["biggest_ride_distance"]
				stats.biggest_climb_elevation_gain=data['biggest_climb_elevation_gain']

				stats.ytd_count=y["count"]
				stats.ytd_distance=round(y["distance"]/1000)
				stats.ytd_moving_time=str(y["moving_time"])
				stats.ytd_elevation_gain=y["elevation_gain"]

				stats.recent_count=b["count"]
				stats.recent_distance=round(b["distance"]/1000)
				stats.recent_moving_time=str(b["moving_time"])
				stats.recent_elevation_gain=b["elevation_gain"]

				stats.total_count=ride["count"]
				stats.total_distance=ride["distance"]
				stats.total_moving_time=ride["moving_time"]
				stats.total_elevation_gain=ride["elevation_gain"]

				stats.save()

				print("Reloaded %s 's stats. Time %s" % (user.firstName, datetime.datetime.now()))
			except KeyError:
				print("did not work, KeyError, printing data")
				print(data)

@background(schedule=2)
def refresh():
	t = removeMe.objects.latest('id').id
	removeMe(name="Duco"+str(t)).save()

def reload(request):
	return HttpResponse("<h1>reload</h1>")

def downloadss(request):
	return render(request=request, template_name='main/downloads.html', context={'mediaFiles': mediaFiles.objects.all} )

def about(request):
	return render(request=request, template_name='main/about.html')


def authorize(request):
	query = request.GET.get('code')
	query2 = request.GET.get('error')
	if query2 == 'access_denied':
		return HttpResponse('Je hebt geen toegang gegeven dus kun je niet deze website gebruiken.')

	if query == None:
		return render(request = request, template_name='main/authorize.html', context={'Users': Users.objects.all, 'statistics': statistics.objects.all})

	r = requests.post(url = "https://www.strava.com/oauth/token", params = {"client_id" : id_client, "client_secret" : secret_client, "grant_type" : "authorization_code", "code" : query}).json()

	if not Users.objects.filter(access_token=r['access_token']).exists() or not Users.objects.filter(ied=r['athlete']['id']).exists():
		access_token = r['access_token']
		refresh_token = r["refresh_token"]
		firstName = r['athlete']['firstname']
		secondName = r['athlete']['lastname']
		profilePhoto = str(r['athlete']['profile'])
		ied = str(r['athlete']['id'])
		person = str(r['athlete']['firstname'])
		expires_at = int(r["expires_at"])
		athlete = "https://www.strava.com/athletes/" + ied

		r2 = requests.get("https://www.strava.com/api/v3/athletes/" + ied + "/stats?access_token=" + access_token + "&per_page=1000").json()
		ride = r2["all_ride_totals"]
		y = r2["ytd_ride_totals"]
		b = r2["recent_ride_totals"]

		a = Users(ytd_distance= round(y["distance"]/1000), access_token=access_token, firstName=firstName,secondName=secondName, profilePhoto=profilePhoto, ied=ied, athlete=athlete, refresh_token=refresh_token, expires_at=expires_at)
		a.save()

		a2 = statistics(ied=ied, biggest_ride_distance=r2["biggest_ride_distance"], biggest_climb_elevation_gain=r2["biggest_climb_elevation_gain"], athlete=person, total_distance=ride["distance"], total_elevation_gain=ride["elevation_gain"], total_moving_time=ride["moving_time"], total_count=ride["count"], ytd_count=y["count"], ytd_distance=round(y["distance"]/1000), ytd_moving_time=y["moving_time"], ytd_elevation_gain=y["elevation_gain"], recent_elevation_gain=b["elevation_gain"], recent_distance=round(b["distance"]/1000), recent_moving_time=b["moving_time"], recent_count=b["count"])
		a2.save()

	return render(request = request, template_name='main/authorize.html', context={'Users': Users.objects.all, 'statistics': statistics.objects.all})

def welcome(request):
	query = request.GET.get("refresh")
	if query:
		refreshData(True)
	else:
		refreshData(False)

	return render(request= request, template_name='main/welcome.html', context={'Users': Users.objects.all, 'statistics': statistics.objects.all})

def disclaimer(request):
	return render(request = request, template_name = "main/disclaimer.html")

def donated(request):
	return render(request = request, template_name='main/donate.html') 

def fail-donated(request):
	return render(request= request, template_name='main/fail-donate.html'
