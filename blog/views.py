from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import datetime

# Create your views here.
def home(request):
	now = datetime.datetime.now()
	return render_to_response('Compodoc - The missing documentation tool for your Angular application.htm',{'time':now},context_instance=RequestContext(request))