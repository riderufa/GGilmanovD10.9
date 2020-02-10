from django import forms
from django.forms import ModelForm
from carslist.models import *

class CarForm(ModelForm):
    producer = forms.ModelChoiceField(queryset=Producer.objects.all(), required=False, label='Производитель')
    car_model = forms.ModelChoiceField(queryset=CarModel.objects.select_related("producer").all(), required=False)
    year = forms.IntegerField(required=False)
    description = forms.CharField(widget=forms.widgets.TextInput(), required=False)
    transmission = forms.ChoiceField(required=False)

    class Meta:
        model = Car
        fields = {'producer', 'car_model', 'year', 'description', 'transmission', 'color'}
