from django.shortcuts import render
from django.views.generic import ListView, FormView
from carslist.models import *
from carslist.forms import CarForm
from django.db.models import Q


class CarListView(FormView, ListView):
    model = Car
    form_class = CarForm
    context_object_name = 'cars'
    template_name = 'carslist/car_list.html'


    def get_queryset(self):
        search_query = self.request.GET.get('search-car', '')
        search_form = self.request.GET
        query = Q()
        for key, value in search_form.items():
            if value and key in vars(Car):
                query |= Q(**{key: value})
        if search_form:
            return Car.objects.select_related("producer").select_related("color").prefetch_related("car_model").filter(query)
            # return Car.objects.select_related("producer").select_related("color").prefetch_related("car_model").filter(Q(producer__title__contains=search_query) | Q(car_model__title__contains=search_query) | Q(year__contains=search_query) | Q(color__name__contains=search_query) | Q(transmission__contains=search_query))
        return Car.objects.select_related("producer").select_related("color").prefetch_related("car_model").all()

