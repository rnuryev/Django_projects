from django import forms
# from .models import RzdTenders

# class RzdTendersForm(forms.ModelForm):
#
#     class Meta:
#         model = RzdTenders
#         fields = ('url', 'query_string', 'bid_deadlin_from')

class RzdTendersAdditionForm(forms.Form):
    addition_query = forms.CharField(max_length=350)

