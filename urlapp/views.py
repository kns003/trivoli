from django.shortcuts import render
import json
from django.http import HttpResponseRedirect, HttpResponse
from urlapp.forms import TravelForm, FileUploadForm
from urlapp.models import Travel
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def create_travel(request):
	if request.method == 'POST':
		form = TravelForm(request.POST)
		if form.is_valid():
			travel = Travel(url=form.cleaned_data['url'],
			                url_name=form.cleaned_data['url_name'])
			travel.save()
			return HttpResponseRedirect('/travel/view/')
	else:
		form = TravelForm()
	return render(request, 'create_travel.html', {'form': form})

def view_travel(request):
	travels = Travel.objects.all()
	return render(request, 'view_travel.html', {'travels': travels})

def handle_travel(request, travel_id):
	travel = Travel.objects.get(id=travel_id)
	if request.method == 'POST':
		form = TravelForm(request.POST)
		if form.is_valid():
			travel.url = form.cleaned_data['url']
			travel.url_name = form.cleaned_data['url_name']
			travel.save()
			return HttpResponseRedirect('/travel/view/')
	else:
		data = {'url': travel.url, 'url_name':travel.url_name}
		form = TravelForm(data)

	return render(request, 'create_travel.html', {'form': form, 'travel': travel})

def load_travel(request, travel_id):
	travel = Travel.objects.get(id=travel_id)
	return render(request, 'load_travel.html', {'travel': travel})

def delete_travel(request, travel_id):
	travel = Travel.objects.get(id=travel_id)
	travel.delete()
	return HttpResponseRedirect('/travel/view/')

@csrf_exempt
def create_from_file(request):
	if request.method == 'POST':
		print(request.FILES)
		form = FileUploadForm(request.POST, request.FILES)
		if form.is_valid():
			for line in request.FILES['file'].readlines():
				print(line.decode('utf-8'))
				line = line.decode('utf-8')
				data = line.split(',')
				travel= Travel(url=data[0], url_name=data[1])
				travel.save()
			return HttpResponseRedirect('/travel/view/')

	else:
		form = FileUploadForm()
	return render(request, 'create_from_file.html', {'form': form})