from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms

from .models import Brand, Engine


class AddCarForm(forms.ModelForm):
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
                Column('engine', css_class='form-group col-md-6 mb-0'),
                Column('body_type', css_class='form-group col-md-6 mb-0'),
                Column('year', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )

    brand = forms.ChoiceField(choices=Brand.objects.get(),)
    model = forms.CharField(max_length=50, required=True)
    engine = forms.ChoiceField(choices=Engine.objects.get(),)
    engine_capacity = forms.FloatField(required=False)
    body_type = forms.CharField(max_length=50, required=True)
    power = forms.IntegerField(required=True)
    year = forms.IntegerField(required=True)
