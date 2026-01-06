from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils import timezone
# Create your models here.
class Booking(models.Model):
    name=models.CharField(max_length=255)
    email = models.EmailField(max_length=100, blank=True, null=True)
    booking_date = models.DateTimeField(default=timezone.now)
    no_of_guests=models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)]
    )
    
    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    APPETIZER = "appetizer"
    MAIN = "main"
    DESSERT = "dessert"

    CATEGORY_CHOICES = [
        (APPETIZER, "Appetizers"),
        (MAIN, "Main Courses"),
        (DESSERT, "Desserts"),
    ]

    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    inventory=models.SmallIntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=MAIN)
    menu_image = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f"{self.title} : {self.price}"
    
class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"