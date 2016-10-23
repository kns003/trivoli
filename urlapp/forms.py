from django import forms
from django.forms import ModelForm
from urlapp.models import Travel

class TravelForm(ModelForm):
	class Meta:
		model = Travel
		fields = ['url', 'url_name']

class FileUploadForm(forms.Form):
	file = forms.FileField(
		label='Select a file',
	)