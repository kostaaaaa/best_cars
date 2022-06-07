from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from django.urls import reverse_lazy

from .models import Brand


class AddCarForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('brand', css_class='form-group col-md-6 mb-0'),
                Column('model', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('engine_type', css_class='form-group col-md-6 mb-0'),
                Column('body_type', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('engine_capacity', css_class='form-group col-md-4 mb-0'),
                Column('power', css_class='form-group col-md-4 mb-0'),
                Column('year', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )

    brand_choices = ((x.name, x.name) for x in Brand.objects.all())
    engine_type_choices = (
        ('Benzin', 'Benzin'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric')
        )
    body_type_choices = (
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('Touring', 'Touring'),
        ('Coupe', 'Coupe'),
        ('Minivan', 'Minivan'),
        ('Bus', 'Bus')
        )
    brand = forms.ChoiceField(choices=brand_choices)
    model = forms.CharField(max_length=50, required=True)
    engine_type = forms.ChoiceField(choices=engine_type_choices)
    engine_capacity = forms.FloatField(required=False)
    body_type = forms.ChoiceField(choices=body_type_choices)
    power = forms.IntegerField(required=True)
    year = forms.IntegerField(required=True)
