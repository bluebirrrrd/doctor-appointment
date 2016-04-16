from django.shortcuts import render

from .forms import AppointmentForm


def new_appointment(request):
    form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})
