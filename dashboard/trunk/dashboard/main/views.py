# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from django.conf import settings

import datetime
import dateutil.parser as p

# for google map
from django import forms
from gmapi import maps # easy_install django-gmapi
from gmapi.forms.widgets import GoogleMap

from dashboard.main.models import Tweet


class MapForm(forms.Form):
	map = forms.Field(widget=GoogleMap(attrs={'width':600, 'height':450}))


MOODCOLOR = { "anger" : "ea5148", 
	      "disgusted" : "8ae65f",
	      "joy" : "ffc334",
	      "sadness" : "2c60c8",
	      "surprised" : "fa9d4d" }


def fetch_results(request):
	age_band = "all"
	gender = "all"
	race = "all"
	mood = "all"
	date_from = (datetime.datetime.now() - datetime.timedelta(days=180)).strftime("%d-%b-%Y")
	date_to = datetime.datetime.now().strftime("%d-%b-%Y")
	if request.GET.has_key("age_band"):
		age_band = request.GET["age_band"]
	if request.GET.has_key("gender"):
		gender = request.GET["gender"]
	if request.GET.has_key("race"):
		race = request.GET["race"]
	if request.GET.has_key("mood"):
		mood = request.GET["mood"]
	if request.GET.has_key("date_to"):
		date_to = request.GET["date_to"]
	if request.GET.has_key("date_from"):
		date_from = request.GET["date_from"]
		
	return fetch_results_inner(age_band,gender,race,mood, date_from, date_to)

def fetch_results_inner(age_band,gender,race,mood,date_from,date_to):
	if date_from == "" or date_to == "":
		date_from = None
		date_to = None
	else:
		try:
			date_from = p.parse(decode_html(date_from))
			date_to =  p.parse(decode_html(date_to))
		except:
			date_from = None
			date_to =  None

	if ((date_from is None) or (date_to is None)):
		results = Tweet.objects.all()
	else:
		results = Tweet.objects.filter(time_posted__gte=date_from, time_posted__lt=(date_to + datetime.timedelta(days=1)))
	if (age_band != "all"):
		results = results.filter(age_band = age_band)
	if (gender != "all"):
		results = results.filter(gender=gender.upper())
	if (race != "all"):
		results = results.filter(race=race.upper())
	if (mood != "all"):
		results = results.filter(mood=mood)
	return results

def home_redirect(request):
	return redirect('main/')

def decode_html(s):
	return s.replace('%2F','/')

def home(request):
	age_band = "all"
	gender = "all"
	race = "all"
	mood = "all"
	date_from = (datetime.datetime.now() - datetime.timedelta(days=180)).strftime("%d-%b-%Y")
	date_to = datetime.datetime.now().strftime("%d-%b-%Y")

	if request.GET.has_key("age_band"):
		age_band = request.GET["age_band"]
	if request.GET.has_key("gender"):
		gender = request.GET["gender"]
	if request.GET.has_key("race"):
		race = request.GET["race"]
	if request.GET.has_key("mood"):
		mood = request.GET["mood"]
	if request.GET.has_key("date_to"):
		date_to = request.GET["date_to"]
	if request.GET.has_key("date_from"):
		date_from = request.GET["date_from"]
		
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
		'center': maps.LatLng(1.263347, 103.823242),
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
		# mesg = "%s <br/> joy : %d <br/> surprised : %d <br/> sadness : %d <br/> anger : %d <br/> disgusted : %d" % (key, val["joy"], val["surprised"], val["sadness"], val["anger"], val["disgusted"])
		mesg = "%s <br/> <img src='https://chart.googleapis.com/chart?chco=%s,%s,%s,%s,%s&cht=p&chd=t:%d,%d,%d,%d,%d&chs=300x120&chdl=joy|surprised|sadness|anger|disgusted&chl=%d|%d|%d|%d|%d'/>" % (key, MOODCOLOR["joy"], MOODCOLOR["surprised"], MOODCOLOR["sadness"], MOODCOLOR["anger"], MOODCOLOR["disgusted"], val["joy"], val["surprised"], val["sadness"], val["anger"], val["disgusted"], val["joy"], val["surprised"], val["sadness"], val["anger"], val["disgusted"])
		info = maps.InfoWindow({
			'content': mesg ,
			'disableAutoPan': True
			})
		info.open(gmap, marker)


	context = {'form': MapForm(initial={'map': gmap}),
		   'gender': gender,
		   'age_band' : age_band,
		   'race' : race,
		   'mood' : mood,
		   'date_to': date_to,
		   'date_from' :date_from,
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



def tweet_ajax(request,page_index,page_size):
	results = fetch_results(request).order_by("-time_posted")
	page_index = int(page_index)
	page_size = int(page_size)
	tweets = []
	
	style = "even"
	for result in results:
		tweets.append({ "text" : mask_sensitive(result.tweet.replace('\/','/')), "mood" : result.mood, "style" : style, "time_posted": result.time_posted.strftime("%d-%b-%Y %H:%M:%S %a")})
		if style == "even":
			style = "odd"
		else:
			style = "even"
	tweets = tweets[(page_index*page_size):((page_index+1)*page_size)]
	return HttpResponse(simplejson.dumps(tweets))


def tweet_total_ajax(request, page_size):
	page_size = int(page_size)
	results = fetch_results(request)
	value = { "total" : len(results),
		  "page_total" : len(results) / page_size }
	return HttpResponse(simplejson.dumps(value))


def mood_ajax(request, age_band, gender, race, mood, date_from, date_to):
	results = fetch_results_inner(age_band, gender, race, mood, date_from, date_to)
	dict = { "joy": 0, "surprised": 0, "disgusted":0 , "sadness":0, "anger":0}
	for result in results:
		dict[result.mood] += 1
	context = { "mood": dict }
	return render_to_response('main/mood.xml', context)

def profile_ajax(request, age_band, gender, race, mood, date_from, date_to, dimension):
	results = fetch_results_inner(age_band, gender, race, mood, date_from, date_to)

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
	final = []
	i = 0
	colors = ["74ACD1","738DD1","D1737D","D1C773","A2A2A2","1E425A", "D173AB", "C773D1" ]
	for key,value in dict.items():
		final.append( { "name" : key, "count": value, "style" : colors[i] })
		i+=1
	final.sort(lambda x,y:cmp(x["name"],y["name"]))
	context = { "final" : final,
		    "dimension" : dimension,
		    "dimension_name" : dimension.replace('_', ' ')}
	return render_to_response('main/profile.xml', context)


mask_mapping = {
	'bangalas':'sweaty people' 
	}


def mask_sensitive(sentence):
	x = sentence
	for key,value in mask_mapping.items():
		x = x.replace(key,value)
	return x


def trend_ajax(request, age_band, gender, race, mood, date_from, date_to):
	results = fetch_results_inner(age_band, gender, race, mood, date_from, date_to).order_by("time_posted")

	data = {}

	for r in results:
		d = r.time_posted.date()
		if data.has_key(d):
			data[d]['total'] +=1
			data[d][r.mood] +=1
		else:
			data[d] = { 'date' : d.strftime("%d-%b-%Y"), 'total' : 1, 'joy': 0, 'sadness' : 0, 'anger' : 0, 'disgusted' : 0, 'surprised' :0 }
			data[d][r.mood] = 1

	context = { "data" : sorted(data.values(), lambda x,y:cmp(x['date'],y['date'])),
		    "color" : MOODCOLOR,
		    }
	return render_to_response('main/trend.xml', context)	


def wday_ajax(request, age_band, gender, race, mood, date_from, date_to):
	results = fetch_results_inner(age_band, gender, race, mood, date_from, date_to)

	data = {}
	
	for r in results:
		m = r.mood
		if not (data.has_key(m)):
			data[m] = { 'mood' : m, 'weekday' : 0, 'weekend' : 0 , 'color' : MOODCOLOR[m] }
		if r.day_type.lower() == "weekend":
			data[m]['weekend'] +=1
		else:
			data[m]['weekday'] +=1

	context = { "data" : data.values() }

	return render_to_response('main/wday.xml', context)
			
