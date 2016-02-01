from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from gallery.models import GalleryPage
from conversations.models import ConversationsPage


class HomePage(Page):
	parent_page_types = []
	subpage_types = ['gallery.GalleriesPage', 'conversations.ConversationsPage']

	def home(self):
		return True

	
	def galleries(self):
		if GalleryPage.objects.all():
			return GalleryPage.objects.all()
		else:
			return False

	def conversations(self):
		if ConversationsPage.objects.all():
			return ConversationsPage.objects.all()
		else:
			return False
    
