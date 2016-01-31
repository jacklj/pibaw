from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock


# Create your models here.
class ConversationsPage(Page):
	page_title = models.CharField(max_length=255)
	main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
	intro = RichTextField(blank=True)

	content_panels = Page.content_panels + [
	    FieldPanel('page_title'),
	    ImageChooserPanel('main_image'),
	    FieldPanel('intro'),
	]

	@property
	def conversations(self):
		if ConversationPage.objects.all():
			return ConversationPage.objects.all()
		else:
			return False
	
	# template = 'conversations_page.html'

	parent_page_types = ['home.HomePage']
	subpage_types = ['conversations.ConversationPage']


class ConversationPage(Page):
	date = models.DateField("Post date")
	body = StreamField([
	    ('heading', blocks.CharBlock(classname="full title")),
	    ('paragraph', blocks.RichTextBlock()),
	    ('image', ImageChooserBlock()),
	])


	content_panels = Page.content_panels + [
	    FieldPanel('date'),
	    StreamFieldPanel('body'),
	]

	parent_page_types = ['conversations.ConversationsPage']
	subpage_types = []





