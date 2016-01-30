from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from gallery.models import GalleryPage


class HomePage(Page):

	@property 
	def galleries(self):
		if GalleryPage.objects.all():
			return GalleryPage.objects.all()
		else:
			return False
    
