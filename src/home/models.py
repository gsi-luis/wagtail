from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class HomePage(Page):

    # Database fields
    author = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField(default=None, null=True, blank=True)
    date = models.DateField("Post date", default=None, null=True, blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('author'),
        index.FilterField('date'),
    ]


    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('body', classname="full"),
        InlinePanel('related_links', label="Related links"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('feed_image'),
    ]


    # Parent page / subpage type rules
    parent_page_types = ['home.HomePage']
    subpage_types = []


class HomePageRelatedLink(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]
