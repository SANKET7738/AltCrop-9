from django import forms
from .models import CropDetails

state_choices = CropDetails.objects.values_list('State_Name').distinct()

class InputForm(forms.Form):
    State_Name = forms.ModelChoiceField(
        queryset=CropDetails.objects.values_list('State_Name',flat=True).distinct(),
        empty_label="State",
        label='')
    District_Name = forms.ModelChoiceField(
        queryset=CropDetails.objects.values_list('District_Name',flat=True).distinct(),
        empty_label="District",
        label='')
    
class TestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['State_Name'] = forms.ModelChoiceField(
            queryset=CropDetails.objects.values_list('State_Name',flat=True).distinct(),
            empty_label="State"
        )
        self.fields['District_Name'] = forms.ModelChoiceField(
            queryset=CropDetails.objects.values_list('District_Name',flat=True).filter(State_Name=State_Name).distinct(),
            empty_label="District"
        )


'''
        def __init__(self, *args, **kwargs):
            super(InputForm, self).__init__(*args, **kwargs)
        self.fields['District_Name'].queryset = CropDetails.objects.values_list('District_Name').filter(State_Name=State_Name)
'''