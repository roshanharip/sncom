from django.db import models
from users.models import PharmacyUser
# Create your models here.
class Clinic(models.Model):
    name = models.CharField(max_length=254, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=254, null=True)
    pincode = models.CharField(max_length=254, null=True)
    district = models.CharField(max_length=254, null=True)
    state = models.CharField(max_length=254, null=True)
    country = models.CharField(max_length=254, null=True)
    doctor = models.CharField(max_length=254, null=True)
    contact = models.CharField(max_length=50, null=True)
    document = models.FileField(upload_to='clinic/doc/', null=True)
    day_from = models.CharField(max_length=15, null=True)
    day_to = models.CharField(max_length=15, null=True)
    time_from = models.TimeField(null=True)
    time_to = models.TimeField(null=True)

class Hospital(models.Model):
    name = models.CharField(max_length=254, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=254, null=True)
    pincode = models.CharField(max_length=254, null=True)
    district = models.CharField(max_length=254, null=True)
    state = models.CharField(max_length=254, null=True)
    country = models.CharField(max_length=254, null=True)
    contact = models.CharField(max_length=50, null=True)
    services = models.TextField( null=True)
    contact_person = models.CharField(max_length=50, null=True)
    document = models.FileField(upload_to='hospital/doc/', null=True)

class Ambulance(models.Model):
    name = models.CharField(max_length=254, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=254, null=True)
    pincode = models.CharField(max_length=254, null=True)
    district = models.CharField(max_length=254, null=True)
    state = models.CharField(max_length=254, null=True)
    country = models.CharField(max_length=254, null=True)
    contact = models.CharField(max_length=50, null=True)
    services = models.TextField( null=True)
    price = models.IntegerField(null=True)
    contact_person = models.CharField(max_length=50, null=True)
    document = models.FileField(upload_to='ambulance/doc/', null=True)

class ImagingCentre(models.Model):
    name = models.CharField(max_length=254, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=254, null=True)
    pincode = models.CharField(max_length=254, null=True)
    district = models.CharField(max_length=254, null=True)
    state = models.CharField(max_length=254, null=True)
    country = models.CharField(max_length=254, null=True)
    contact = models.CharField(max_length=50, null=True)
    services = models.TextField( null=True)
    price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    contact_person = models.CharField(max_length=50, null=True)
    document = models.FileField(upload_to='imagingcentre/doc/', null=True)

class NursingBuero(models.Model):
    name = models.CharField(max_length=254, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=254, null=True)
    pincode = models.CharField(max_length=254, null=True)
    district = models.CharField(max_length=254, null=True)
    state = models.CharField(max_length=254, null=True)
    country = models.CharField(max_length=254, null=True)
    contact = models.CharField(max_length=50, null=True)
    services = models.TextField( null=True)
    contact_person = models.CharField(max_length=50, null=True)
    document = models.FileField(upload_to='nursingbuero/doc/', null=True)

class Physiotherapy(models.Model):
    name = models.CharField(max_length=254, null=True)
    doctor = models.CharField(max_length=254, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=254, null=True)
    pincode = models.CharField(max_length=254, null=True)
    district = models.CharField(max_length=254, null=True)
    state = models.CharField(max_length=254, null=True)
    country = models.CharField(max_length=254, null=True)
    contact = models.CharField(max_length=50, null=True)
    services = models.TextField( null=True)
    contact_person = models.CharField(max_length=50, null=True)
    document = models.FileField(upload_to='physiotherapy/doc/', null=True)

class Pharmacy(models.Model):
    UNIT_CHOICES = [
        ('bundle', 'bundle'),
        ('bottle', 'bottle'),
        ('strip','strip')
    ]
    # user = models.ForeignKey(PharmacyUser, on_delete=models.CASCADE)
    pharmacy = models.EmailField(max_length=254, null=True)
    name = models.CharField(max_length=254, null=True)
    price  = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    quantity = models.CharField(max_length=10, null=True)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, null=True)

class Pathology(models.Model):
    name = models.CharField(max_length=254, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=254, null=True)
    pincode = models.CharField(max_length=254, null=True)
    district = models.CharField(max_length=254, null=True)
    state = models.CharField(max_length=254, null=True)
    country = models.CharField(max_length=254, null=True)
    contact = models.CharField(max_length=50, null=True)
    services = models.TextField( null=True)
    contact_person = models.CharField(max_length=50, null=True)
    document = models.FileField(upload_to='pathology/doc/', null=True)

class PathologyTest(models.Model):
    owner = models.ForeignKey(Pathology, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    price = models.IntegerField(null=True)
    details  = models.TextField(null=True)
    discount = models.IntegerField(null=True)

class Delivery(models.Model):
    name  = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=254, null=True)
    pincode = models.CharField(max_length=254, null=True)
    district = models.CharField(max_length=254, null=True)
    state = models.CharField(max_length=254, null=True)
    country = models.CharField(max_length=254, null=True)
    contact = models.CharField(max_length=50, null=True)
    is_avail = models.BooleanField(default=True)
    doc_of_id = models.FileField(upload_to='delivery/docId/', null=True)
    doc_of_license = models.FileField(upload_to='delivery/docLicense/' , null=True)

