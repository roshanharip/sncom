from django.contrib import admin
from .models import Pharmacy, ImagingCentre, Ambulance, NursingBuero, Hospital, Clinic, Pathology, PathologyTest, Physiotherapy, Delivery
# Register your models here.
admin.site.register(Pharmacy)
admin.site.register(ImagingCentre)
admin.site.register(Ambulance)
admin.site.register(NursingBuero)
admin.site.register(Hospital)
admin.site.register(Clinic)
admin.site.register(Pathology)
admin.site.register(PathologyTest)
admin.site.register(Physiotherapy)
admin.site.register(Delivery)
