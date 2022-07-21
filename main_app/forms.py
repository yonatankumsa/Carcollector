from django.forms import ModelForm
from .models import Mods

class ModsForm(ModelForm):
  class Meta:
    model = Mods
    fields = ['mod', 'power']