from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import MenuItem, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
def index(request):
 return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})

class MenuItemsView(generics.ListCreateAPIView):
  #permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuSerializer