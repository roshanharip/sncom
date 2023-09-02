from django.contrib import admin
from .models import UserAccount , CustomerUser, PharmacyUser, StaffUser
# Register your models here.



admin.site.register(UserAccount)
admin.site.register(CustomerUser)
admin.site.register(PharmacyUser)
admin.site.register(StaffUser)





