from django import forms
from django.forms import ModelForm
from carslist.models import *

class CarForm(ModelForm):
    # producer = forms.ChoiceField(required=False, label='Производитель')
    producer = forms.ModelChoiceField(queryset=Producer.objects.all(), required=False, label='Производитель')

    # car_model = forms.ChoiceField(required=False)
    car_model = forms.ModelChoiceField(queryset=CarModel.objects.select_related("producer").all(), required=False)
    year = forms.IntegerField(required=False)
    description = forms.CharField(widget=forms.widgets.TextInput(), required=False)
    transmission = forms.TypedChoiceField(choices=[('A', 'automatic'), ('M', 'manual'), (None, '---------')], required=False)
    field_order = ['producer', 'car_model', 'color', 'year', 'description', 'transmission']

    class Meta:
        model = Car
        fields = {'producer', 'car_model', 'color', 'year', 'description', 'transmission'}
