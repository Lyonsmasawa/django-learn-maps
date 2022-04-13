from django import forms    
from .models import Measurement

class MeasurmentsForm(forms.ModelForm):
    """Form definition for Measurments."""

    class Meta:
        """Meta definition for Measurmentsform."""

        model = Measurement
        fields = ('destination',)
