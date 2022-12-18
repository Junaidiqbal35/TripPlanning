# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.db import IntegrityError, transaction

from core.forms import ActivityFormSet
from core.models import TripPlace, Activity


class TripListView(ListView):
    template_name = "home.html"
    queryset = TripPlace.objects.all()
    context_object_name = 'tripe_place'
    model = TripPlace
    slug_field = 'id'

    def get_queryset(self):
        # Search on place name
        if self.request.GET.get('search'):
            query = self.request.GET.get('search')
            # i-contains lookup is case-insensitive
            self.queryset = TripPlace.objects.filter(place_name__icontains=query)
            return self.queryset

        return self.queryset


class TripDetailView(DetailView):
    template_name = "place_detail.html"
    queryset = TripPlace.objects.all()
    context_object_name = 'tripe_place'
    model = TripPlace
    slug_field = 'id'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class TripPlanCreate(LoginRequiredMixin, CreateView):
    model = TripPlace
    template_name = 'create_trip_plan.html'
    fields = ['place_name', 'number_of_days_trip', 'place_image']

    def get_context_data(self, **kwargs):
        data = super(TripPlanCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['trip_form'] = ActivityFormSet(self.request.POST, self.request.FILES)
        else:
            data['trip_form'] = ActivityFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        trip_form_data = context['trip_form']
        with transaction.atomic():
            self.object = form.save(commit=False)
            self.object.trip_uploader = self.request.user
            self.object.save()

            if trip_form_data.is_valid():
                trip_form_data.instance = self.object
                trip_form_data.save()
        return super(TripPlanCreate, self).form_valid(form)
