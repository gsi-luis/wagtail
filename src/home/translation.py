from .models import HomePage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from wagtail.core.models import Page



@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
        'body',
    )