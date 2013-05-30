from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def index(request):
	now = datetime.datetime.now()
	t = get_template('index.html')
	html = t.render(Context({'current_datetime':now}))
	return HttpResponse(html)

def about(request):
	now = datetime.datetime.now()
	t = get_template('about.html')
	html = t.render(Context({'current_datetime':now}))
	return HttpResponse(html)

def blog(request):
	return render_to_response('blog.html')

def projects(request):
	return render_to_response('projects.html')

def contact(request):
	return render_to_response('contact.html')
	
def specific_blog(request):
	return render_to_response('blog.html')
	
def hello(request):
	return HttpResponse("Hello world")
	
def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date':now}))
	#html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
	
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)