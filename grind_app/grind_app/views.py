from django.http import HttpResponse
from django.shortcuts import render_to_response

import logging

def test_page(request):
	return render_to_response('templates/test-page.html')
