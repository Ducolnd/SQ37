from django.db import models
from django.utils import timezone

# Create your models here.

class Users(models.Model):
	access_token = models.CharField('access_token',max_length=200, default='geen')
	refresh_token = models.CharField('refresh_token', max_length=200, default='geen')
	firstName = models.CharField('firstName',max_length=200, default='geen')
	secondName = models.CharField('secondName',max_length=200, default='geen')
	ied = models.CharField('ied',max_length=200, default='geen')
	profilePhoto = models.CharField('profilePhoto',max_length=200, default='geen')
	athlete = models.CharField('athlete', max_length=200, default='https://www.strava.com/athletes/41206887')
	expires_at = models.IntegerField('expires_at', default=1)
	ytd_distance = models.IntegerField('distance', default = 0)

	def __str__(self):
		return self.firstName

class statistics(models.Model):
	#Most 
	biggest_ride_distance = models.IntegerField('biggest_ride_distance', default=0)
	biggest_climb_elevation_gain = models.IntegerField('biggest_climb_elevation_gain', default=0, null = True)
	#Total
	total_distance = models.IntegerField('total_distance', default=0)
	total_elevation_gain = models.IntegerField('total_elevation_gain', default=0)
	total_moving_time = models.IntegerField('total_moving_time', default=0)
	total_count = models.IntegerField('total_count', default=0)
	#Year-To-Date:
	ytd_count = models.IntegerField('ytd_count', default=0)
	ytd_distance = models.IntegerField('ytd_distance', default=0)
	ytd_moving_time = models.CharField('ytd_moving_time', max_length=14, default="00:00:00")
	ytd_elevation_gain = models.IntegerField('ytd_elevation_gain', default=0)
	#Recent / maand
	recent_count = models.IntegerField('recent_count', default=0)
	recent_distance = models.IntegerField('recent_distance', default=0)
	recent_moving_time = models.CharField('recent_moving_time', max_length=14, default="00:00:00")
	recent_elevation_gain = models.IntegerField('recent_elevation_gain', default=0)


	athlete = models.CharField('athlete', max_length=200, default="None")
	ied = models.IntegerField('ied', default=0)

	def __int__(self):
		return self.athlete

class mediaFiles(models.Model):
	title = models.CharField('title', max_length=100, default="Geen titel benoemd")
	text = models.TextField('text', default="Geen beschrijving benoemd")
	date = models.DateTimeField('date', default=timezone.now)
	file = models.FileField('file')
	img = models.ImageField('img')

	def __str__(self):
		return self.title
