from django import forms
from .models import UserBookRate
from django.core.validators import MaxValueValidator, MinValueValidator


class RateForm(forms.Form):
    rate = forms.ChoiceField(choices=UserBookRate.RATE_CHOICES, widget=forms.Select(), required=True,
                             validators=[MaxValueValidator('5'), MinValueValidator('1')])

    class Meta:
        model = UserBookRate
        fields = '__all__'
