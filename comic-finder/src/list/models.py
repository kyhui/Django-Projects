from django.db import models

# Create your models here.
class Manga(models.Model):
	name = models.CharField(max_length = 80, blank = False, primary_key = True)
	chapter = models.IntegerField(blank = False, null = False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.name