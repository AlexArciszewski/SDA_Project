from django.forms import ModelForm
from .models import Covidians



class CovidiansForm(ModelForm):
    class Meta:
        model = Covidians
        fields = ["id", "name", "email", "tested_positive", "shots_taken", "user_photo"] #można tez exlude i podac te które chcemy wyrzucić[]