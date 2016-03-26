from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                InlinePanel,
                                                MultiFieldPanel,
                                                PageChooserPanel)

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

# Create your models here.

class GalleriesPage(Page):
	parent_page_types = ['home.HomePage']
	subpage_types = ['gallery.GalleryPage']



class GalleryPage(Page):
	# page_title = models.CharField(max_length=255, help_text="Left half of title", blank=True)
	# title_right = models.CharField(max_length=255, help_text="Right half of title", blank=True)
	template = 'gallery/gallery_page2.html'

	# main_image = models.ForeignKey(
 #        'wagtailimages.Image',
 #        null=True,
 #        blank=True,
 #        on_delete=models.SET_NULL,
 #        related_name='+'
 #    )

	@property 
	def pictures(self):
		if self.gallery_pictures.all():
			return self.gallery_pictures.all()
		else:
			return False

	content_panels = Page.content_panels + [
		# FieldPanel('page_title'),
		# ImageChooserPanel('main_image'),
		# FieldPanel('title_right'),
		InlinePanel('gallery_pictures', label="Pictures"),
	]

	parent_page_types = ['gallery.GalleriesPage']
	subpage_types = []


class Picture(Orderable):
	title =  models.CharField(max_length=255, blank=True)
	description =  RichTextField(blank=True)
	
	image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

	panels = [
		FieldPanel('title'),
		FieldPanel('description'),
		ImageChooserPanel('image'),
	]


	def __str__(self):
		return self.title

	page = ParentalKey(
		'GalleryPage', 
		related_name='gallery_pictures', 
		on_delete=models.SET_NULL,
		null=True,
        blank=True,
		)