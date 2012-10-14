# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

import datetime


def home(request):
	context = {
		}
	return render_to_response(
		'main/home.html',
		context,
		context_instance=RequestContext(request),
	)
