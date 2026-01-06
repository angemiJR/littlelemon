from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    booking_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        input_formats=[
            "%Y-%m-%dT%H:%M",      # 2025-12-18T14:30
            "%Y-%m-%dT%H:%M:%S",   # 2025-12-18T14:30:00 (some browsers)
        ],
    )

    class Meta:
        model = Booking
        fields = ["name", "email", "booking_date", "no_of_guests"]

