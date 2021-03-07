from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django import forms


class CreateEventForm(forms.Form):
    date = forms.DateTimeField(
        widget=DatePickerInput(format='%m/%d/%Y')
    )
    time_start = forms.TimeField(
        widget=TimePickerInput()
    )
    time_end = forms.TimeField(
        widget=TimePickerInput()
    )