from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CarSerializer,Car,ReservationSerializer, Reservation
# from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReadOnly
from django.db.models import Q,Exists,OuterRef                 #! or lu kullanim icin .....
# Create your views here.


class CarView(ModelViewSet):
    serializer_class=CarSerializer
    queryset=Car.objects.all()
    permission_classes=[IsAdminOrReadOnly]
#! 2508 elde ettigimiz queryseti degistirmeye calisiyourz. tarihlerden olusan slug icin. reservationdaki arabalara ulasip onlari ayiklamam lazim.
    def get_queryset(self):
        if self.request.user.is_staff:
            queryset=super().get_queryset().filter()
        else:
            queryset=super().get_queryset().filter(availability=True)
        start=self.request.query_params.get("start")   #!gelen istekteki starti al sakla.
        end=self.request.query_params.get("end")

        if start and end:
            #!way-1
            # not_available = Reservation.objects.filter(end_date__gt=start, start_date__lt=end).values_list('id',flat=True)
            #!way-2 with and , or
            c1=Q(end_date__gt=start)
            c2=Q(start_date__lt=end)
            
            # not_available=Reservation.objects.filter(
            #     c1 | c2
            #     ).values_list('id',flat=True)

            # not_available=Reservation.objects.filter(
            #     c1 & c2
            #     ).values_list('id',flat=True)

            # queryset=queryset.exclude(id__in=not_available)
            
            #! with annotate ile kullanimi filter yerine. is_available serializersta da tanimlanmali
            #!SQL deki join yapisi
            queryset=queryset.annotate(
                is_available= ~Exists(Reservation.objects.filter(
                    Q(car=OuterRef('pk')) & c1 & c2
                    )
                )
            )


        return queryset
    
#!flat true idleri [1,3,5] böyle bir listeye ceviriyor.

class ReservationView(ModelViewSet):
    serializer_class=ReservationSerializer
    queryset=Reservation.objects.all()
