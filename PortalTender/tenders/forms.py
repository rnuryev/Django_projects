from django import forms
from .models import RzdTenders

class RzdTendersForm(forms.ModelForm):
    class Meta:
        model = RzdTenders
        fields = ('url', 'query_string', 'bid_deadlin_from')

