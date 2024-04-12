from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='static/images', blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    def get_absolute_url(self):
        return reverse('agent_detail', kwargs={'pk': self.pk})


class Neighborhood(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PropertyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SaleStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class PriceRange(models.Model):
    lower_bound = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Lower Bound"))
    upper_bound = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Upper Bound"))
    description = models.CharField(max_length=200, blank=True, verbose_name=_("Description"))

    def __str__(self):
        return f"{self.lower_bound} to {self.upper_bound}"


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, verbose_name=_("Neighborhood"))
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, verbose_name=_("Property Type"))
    sale_status = models.ForeignKey(SaleStatus, on_delete=models.CASCADE, verbose_name=_("Sale Status"))
    price_range = models.ForeignKey(PriceRange, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name=_("Price Range"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    city = models.CharField(max_length=100, verbose_name=_("City"))
    state = models.CharField(max_length=100, verbose_name=_("State"))
    zip_code = models.CharField(max_length=12, verbose_name=_("ZIP/Postal Code"))
    is_featured = models.BooleanField(default=False, verbose_name=_("Featured"))
    visibility = models.BooleanField(default=True, verbose_name=_("Visible"))
    bedroom_count = models.IntegerField(verbose_name=_("Bedrooms"))
    bathroom_count = models.IntegerField(verbose_name=_("Bathrooms"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    photo1 = models.ImageField(upload_to='listing_photos/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='listing_photos/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='listing_photos/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='listing_photos/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.price_range = self.determine_price_range()
        super().save(*args, **kwargs)

    def determine_price_range(self):
        ranges = PriceRange.objects.filter(lower_bound__lte=self.price, upper_bound__gte=self.price)
        return ranges.first() if ranges.exists() else None

    def __str__(self):
        return f'{self.address}, {self.city}'
