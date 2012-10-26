# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

import datetime

# for google map
from django import forms
from gmapi import maps
from gmapi.forms.widgets import GoogleMap




def home(request):
	context = {
		}
	return render_to_response(
		'main/home.html',
		context,
		context_instance=RequestContext(request),
	)


class MapForm(forms.Form):
	map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))



def map(request):
	gmap = maps.Map(opts = {
		'center': maps.LatLng(1.254347, 103.823242),
		'mapTypeId': maps.MapTypeId.ROADMAP,
		'zoom': 15,
		'mapTypeControlOptions': {
			'style': maps.MapTypeControlStyle.DROPDOWN_MENU
			},
		})
	marker = maps.Marker(opts = {
		'map': gmap,
		'position': maps.LatLng(38, -97),
		})
	maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
	maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
	info = maps.InfoWindow({
		'content': 'Hello!',
		'disableAutoPan': True
		})
	info.open(gmap, marker)
	context = {'form': MapForm(initial={'map': gmap})}
	return render_to_response('main/map.html', context)

