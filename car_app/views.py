from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CarSerializer,Car,ReservationSerializer, Reservation
# from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReadOnly
# Create your views here.


class CarView(ModelViewSet):
    serializer_class=CarSerializer
    queryset=Car.objects.all()
    permission_classes=[IsAdminOrReadOnly]

class ReservationView(ModelViewSet):
    serializer_class=ReservationSerializer
    queryset=Reservation.objects.all()
