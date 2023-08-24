from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
#!!! Choices mantigi su. bu alana yeni veri girme ihtimali var mi(sik bir sekilde)bu yüzden sadece gear choices ile.???

# Create your models here.
class Car(models.Model):

    GEAR=(
        ('a','automatic'),
        ('m','manual')
    )

    plate_number=models.CharField(max_length=20, unique=True)   
    brand=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    year=models.SmallIntegerField()
    gear=models.CharField(max_length=1, choices=GEAR) 
    rent_per_day = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(50)]) 
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand}-{self.model}-{self.plate_number}"
    

class Reservation(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE,related_name='reservations_customer')
    car=models.ForeignKey(Car, on_delete=models.CASCADE, related_name="reservations_car")
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return f"Reservation for {self.car} by {self.customer} from {self.start_date} to {self.end_date}"
    
#! 1 numarali musterinin yapmis oldugu tüm rezervationlara erismek istedigim zaman. related_name="reservation" lazim. line27


