from django.http import HttpResponse
from django.shortcuts import render_to_response

import logging
import json

from eventbrite import EventbriteAPI
from recurly_api import RecurlyAPI

def test_page(request):
	return render_to_response('templates/test-page.html')

def eventbrite_create_event(request):
	api = EventbriteAPI()
	name = request.GET.get('name')
	start_time = request.GET.get('start_time') #format: 2015-10-30T13:00:00Z
	end_time = request.GET.get('end_time')
	response = api.create_event(name, start_time, end_time)
	return HttpResponse(json.dumps(response), content_type="application/json")

def eventbrite_create_tickets(request):
	api = EventbriteAPI()
	name = request.GET.get('name')
	id = request.GET.get('id')
	quantity = request.GET.get('quantity')
	response = api.create_tickets(id, name, quantity)
	return HttpResponse(json.dumps(response), content_type="application/json")

def recurly_get_accounts(request):
	api = RecurlyAPI()
	response = api.get_accounts()
	return HttpResponse(json.dumps(response), content_type="application/json")