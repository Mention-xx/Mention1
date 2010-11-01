from django import forms
from models import Activity

class ActivityForm(forms.ModelForm):
    class Meta(object):
        model = Activity
        exclude = ('delegate',)

