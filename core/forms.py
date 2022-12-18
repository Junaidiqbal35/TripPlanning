from django import forms
from django.forms import inlineformset_factory

from .models import TripPlace, Activity


class TripPlaceForm(forms.ModelForm):
    class Meta:
        model = TripPlace
        fields = ['place_name', 'number_of_days_trip', 'place_image']


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_place_name', 'activity_place_description', 'activity_place_image']


ActivityFormSet = inlineformset_factory(TripPlace, Activity,
                                        form=ActivityForm, extra=3,  can_delete=False)
