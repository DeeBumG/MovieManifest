from django.forms import modelformset_factory
from .models import SiteSetting

SiteSettingFormSet = modelformset_factory(
    SiteSetting,
    fields=('key', 'value'),
    extra=0
)
