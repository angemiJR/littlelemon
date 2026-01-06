from django.shortcuts import render, redirect
from rest_framework import generics, viewsets, permissions
from .models import MenuItem, Booking
from .serializers import MenuSerializer, BookingSerializer
from django.db.models import Case, When, Value, IntegerField
#from rest_framework.decorators import api_view, permission_classes
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.response import Response
from .forms import BookingForm
from django.conf import settings
import os

# Create your views here.
def home(request):
 return render(request, 'index.html', {})

def about(request):
    gallery_dir = os.path.join(
        settings.BASE_DIR, "restaurant", "static", "restaurant", "img", "gallery"
    )

    images = []
    if os.path.isdir(gallery_dir):
        images = sorted([
            f for f in os.listdir(gallery_dir)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        ])

    return render(request, "about.html", {"images": images})

def menu(request):
    items = MenuItem.objects.annotate(
        cat_order=Case(
            When(category=MenuItem.APPETIZER, then=Value(1)),
            When(category=MenuItem.MAIN, then=Value(2)),
            When(category=MenuItem.DESSERT, then=Value(3)),
            output_field=IntegerField(),
        )
    ).order_by("cat_order", "title")

    return render(request, "menu.html", {"items": items})

def booking_page(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("restaurant:book")  # PRG pattern
    else:
        form = BookingForm()

    bookings = Booking.objects.all()
    return render(request, "booking.html", {"form": form, "bookings": bookings})

class MenuItemView(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    

"""@api_view(["GET"])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})

class MenuItemsView(generics.ListCreateAPIView):
  #permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuSerializer """