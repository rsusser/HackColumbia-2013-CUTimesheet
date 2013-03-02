from django import forms
from models import Sheet

#class SheetForm(forms.ModelForm):
#    class Meta:
#        model = Sheet

class SheetForm(forms.Form):
    st1 = forms.TimeField()
    et1 = forms.TimeField()
    st2 = forms.TimeField()
    et2 = forms.TimeField()
