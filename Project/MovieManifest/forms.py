from django.forms import modelformset_factory
from .models import SiteSetting
from django import forms
from django.contrib.auth.forms import UserCreationForm

SiteSettingFormSet = modelformset_factory(
    SiteSetting,
    fields=('key', 'value'),
    extra=0
)


