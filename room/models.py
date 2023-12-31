from django.db import models
from account.models import CITY_CHOICES , DISTRICT_CHOICES ,User
import uuid



ROOM_TYPE_CHOICES=[
    ('Single','Single'),
    ('Double','Double')
]


STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]

# Create your models here.
class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    size = models.IntegerField(help_text='Size in square feet')
    amenities = models.TextField(blank=True, null=True)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Available')
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)

    # Address
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100,choices=CITY_CHOICES)
    district = models.CharField(max_length=100,choices=DISTRICT_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room_type}"
