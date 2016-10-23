from django.db import models

# Create your models here.

class Travel(models.Model):
	url = models.URLField(max_length=500, blank=True, default='')
	url_name = models.CharField(max_length=255,null=True,blank=True)

