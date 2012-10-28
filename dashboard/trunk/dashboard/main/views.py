# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from django.conf import settings

import datetime

# for google map
from django import forms
from gmapi import maps # easy_install django-gmapi
from gmapi.forms.widgets import GoogleMap

from dashboard.main.models import Tweet


class MapForm(forms.Form):
	map = forms.Field(widget=GoogleMap(attrs={'width':450, 'height':450}))



def fetch_results(request):
	age_band = "all"
	gender = "all"
	race = "all"
	if request.GET.has_key("age_band"):
		age_band = request.GET["age_band"]
	if request.GET.has_key("gender"):
		gender = request.GET["gender"]
	if request.GET.has_key("race"):
		race = request.GET["race"]
	return fetch_results_inner(age_band,gender,race)

def fetch_results_inner(age_band,gender,race):
	results = Tweet.objects.all()
	if (age_band != "all"):
		results = results.filter(age_band = age_band)
	if (gender != "all"):
		results = results.filter(gender=gender.upper())
	if (race != "all"):
		results = results.filter(race=race.upper())
	return results

def home(request):
	age_band = "all"
	gender = "all"
	race = "all"
	if request.GET.has_key("age_band"):
		age_band = request.GET["age_band"]
	if request.GET.has_key("gender"):
		gender = request.GET["gender"]
	if request.GET.has_key("race"):
		race = request.GET["race"]	
	results = fetch_results(request)

	# rendering the map # todo figure out a way to put the map into a widget
	# current having a problem with a JS error ":8000/?age_band=all&gender=all&race=all:80 Uncaught TypeError: Cannot read property 'maps' of undefined "
	dict = {}

	for t in results:
		loc = t.location
		if dict.has_key(loc):
			pass
		else:
			dict[loc] = {
				'latitude' : t.latitude,
				'longitude' : t.longitude,
				'sadness' : 0,
				'joy' : 0,
				'anger' : 0,
				'surprised' : 0,
				'disgusted' :0,
				}
		dict[loc][t.mood] += 1
	#print dict 
	gmap = maps.Map(opts = {
		'center': maps.LatLng(1.264347, 103.823242),
		'mapTypeId': maps.MapTypeId.ROADMAP,
		'zoom': 14,
		'mapTypeControlOptions': {
			'style': maps.MapTypeControlStyle.DROPDOWN_MENU
			},
		})
	for key, val in dict.items():
		marker = maps.Marker(opts = {
			'map': gmap,
			'position': maps.LatLng(val["latitude"], val["longitude"]),
			})
		
		maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
		maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
		# mesg = "location : %s <br/> joy : %d <br/> surprised : %d <br/> sadness : %d <br/> anger : %d <br/> disgusted : %d" % (key, val["joy"], val["surprised"], val["sadness"], val["anger"], val["disgusted"])
		mesg = "location : %s <br/> <img src='https://chart.googleapis.com/chart?cht=p&chd=t:%d,%d,%d,%d,%d&chs=300x120&chdl=joy|surprised|sadness|anger|disgusted&chl=%d|%d|%d|%d|%d'/>" % (key, val["joy"], val["surprised"], val["sadness"], val["anger"], val["disgusted"], val["joy"], val["surprised"], val["sadness"], val["anger"], val["disgusted"])
		info = maps.InfoWindow({
			'content': mesg ,
			'disableAutoPan': True
			})
		info.open(gmap, marker)


	context = {'form': MapForm(initial={'map': gmap}),
		   'gender': gender,
		   'age_band' : age_band,
		   'race' : race,
		   'settings' : settings, 
		   }
	return render_to_response(
		'main/home.html',
		context,
		context_instance=RequestContext(request),
	)






def map(request):
	results = fetch_results(request)

	dict = {}

	for t in results:
		loc = t.location
		if dict.has_key(loc):
			pass
		else:
			dict[loc] = {
				'latitude' : t.latitude,
				'longitude' : t.longitude,
				'sadness' : 0,
				'joy' : 0,
				'anger' : 0,
				'surprised' : 0,
				'disgusted' :0,
				}
		dict[loc][t.mood] += 1
	#print dict 
	gmap = maps.Map(opts = {
		'center': maps.LatLng(1.254347, 103.823242),
		'mapTypeId': maps.MapTypeId.ROADMAP,
		'zoom': 14,
		'mapTypeControlOptions': {
			'style': maps.MapTypeControlStyle.DROPDOWN_MENU
			},
		})
	for key, val in dict.items():
		marker = maps.Marker(opts = {
			'map': gmap,
			'position': maps.LatLng(val["latitude"], val["longitude"]),
			})
		
		maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
		maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
		# mesg = "location : %s <br/> joy : %d <br/> surprised : %d <br/> sadness : %d <br/> anger : %d <br/> disgusted : %d" % (key, val["joy"], val["surprised"], val["sadness"], val["anger"], val["disgusted"])
		mesg = "location : %s <br/> <img src='https://chart.googleapis.com/chart?cht=p&chd=t:%d,%d,%d,%d,%d&chs=300x120&chdl=joy|surprised|sadness|anger|disgusted&chl=%d|%d|%d|%d|%d'/>" % (key, val["joy"], val["surprised"], val["sadness"], val["anger"], val["disgusted"], val["joy"], val["surprised"], val["sadness"], val["anger"], val["disgusted"])
		info = maps.InfoWindow({
			'content': mesg ,
			'disableAutoPan': True
			})
		info.open(gmap, marker)


	context = {'form': MapForm(initial={'map': gmap})}
	return render_to_response('main/map.html', context)



def tweet_ajax(request):
	results = fetch_results(request)
	tweets = [ result.tweet for result in results ] 

	return HttpResponse(simplejson.dumps(tweets))


def mood_ajax(request, age_band, gender, race):
	results = fetch_results_inner(age_band, gender, race)
	dict = { "joy": 0, "surprised": 0, "disgusted":0 , "sadness":0, "anger":0}
	for result in results:
		dict[result.mood] += 1
	context = { "mood": dict }
	return render_to_response('main/mood.xml', context)

def profile_ajax(request,dimension):
	results = fetch_results(request)

	dict = {}
	f = lambda x : x.race
	if dimension == "age_band":
		f = lambda x : x.age_band
	elif dimension == "gender":
		f = lambda x : x.gender
	else:
		f = lambda x : x.race
	
	for result in results:
		if dict.has_key(f(result)):
			dict[f(result)] +=1
		else:
			dict[f(result)] =1

	context = { "dict" : dict,
		    "dimension" : dimension,
		    "dimension_name" : dimension.replace('_', ' ')}
	return render_to_response('main/profile.xml', context)