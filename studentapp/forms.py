from django.forms import ModelForm
from studentapp.models import stdmodel

class addform(ModelForm):
    class Meta:
        model = stdmodel
        fields = ['firstname','lastname','course']

