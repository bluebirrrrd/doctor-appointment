from datetime import date

from django import forms
from datetimewidget.widgets import DateTimeWidget

from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('doctor', 'date', 'timeslot', 'patient_name',)
        widgets = {
            'date': DateTimeWidget(
                attrs={'id': 'date'}, usel10n=False, bootstrap_version=3,
                options={
                    'minView': 2,  # month view
                    'maxView': 3,  # year view
                    'weekStart': 1,
                    'todayHighlight': True,
                    'format': 'yyyy-mm-dd',
                    'daysOfWeekDisabled': [0, 6],
                    'startDate': date.today().strftime('%Y-%m-%d'),
                }),
        }
