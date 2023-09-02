from datetime import date

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)

from django.db import models


class UserAccountManager(BaseUserManager):
    
    def create_customer_user(self,email, name, phone_no, password=None, **extrafields):
        extrafields.setdefault('is_customer',True)
        return self.create_user(email,name,phone_no,password,**extrafields)
    
    def create_pharmacy_user(self,email, name, phone_no, password=None, **extrafields):
        extrafields.setdefault('is_pharmacy',True)
        return self.create_user(email,name,phone_no,password,**extrafields)

    def create_staff_user(self,email, name, phone_no, password=None, **extrafields):
        extrafields.setdefault('is_staff',True)
        return self.create_user(email,name,phone_no,password,**extrafields)
    
    def create_user(self,email,name,phone_no, password=None, **extrafields):
        if not email:
            raise ValueError('The Email Field must be set')
        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(email=email,name=name,phone_no=phone_no, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,phone_no,password=None, **extrafields):
        extrafields.setdefault('is_staff',True)
        extrafields.setdefault('is_superuser',True)
        return self.create_user(email, name,phone_no, password, **extrafields)

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=254)
    name = models.CharField(max_length=254, null=True)
    phone_no = models.CharField(max_length=15, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_pharmacy = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone_no']
    
    def __str__(self):
        return self.email
    
    
class CustomerUser(models.Model):
    email = models.EmailField(unique=True, max_length=254)
    customer_id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='customer/customerUserPhoto/',null=True,blank=True)
    gender = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True)
    subscription_start = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    subscription_expiry = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    subscription_title = models.CharField(null=True, max_length=254)
    address = models.TextField(null=True)
    city = models.CharField(null=True, max_length=254)
    def __str__(self) -> str:
        return self.email
    
class PharmacyUser(models.Model):
    email = models.EmailField(unique=True, max_length=254)
    pharmacy_id = models.AutoField(primary_key=True)
    is_approved = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='pharmacy/pharmacyUserPhoto/',null=True,blank=True)
    shop_name = models.CharField(null=True,blank=True, max_length=254)
    address = models.TextField(null=True)
    city = models.CharField(null=True, max_length=254)
    pincode = models.IntegerField(null=True)
    district = models.CharField(null=True, max_length=254)
    state = models.CharField(null=True, max_length=254)
    country = models.CharField(null=True, max_length=254)
    contact_person_name = models.CharField(max_length=254, null=True)
    contact_person_email = models.EmailField(max_length=254, null=True)
    contact_person_phone_no = models.IntegerField(null=True)
    license_no = models.IntegerField(null=True)
    priority = models.IntegerField(default=0, null=True)
    doc_of_license = models.FileField(upload_to='pharmacy/pharmacyUserLicense/', null=True)
    doc_of_ownerId = models.FileField(upload_to='pharmacy/pharmacyUserOwnerId/', null=True)
    doc_of_contactPersonId = models.FileField(upload_to='pharmacy/pharmacyUserContactPersonId/',  null=True)
    def __str__(self) -> str:
        return self.email
class StaffUser(models.Model):
    email = models.EmailField(unique=True, max_length=254)
    staff_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=50, null=True)
    experience = models.FloatField(null=True)
    is_avail = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='staff/staffUserPhoto/', null=True, blank=True)
    description = models.TextField(null=True)
    address = models.TextField(null=True)
    city = models.CharField(null=True, max_length=254)
    document = models.FileField(upload_to='staff/staffDoc', null=True, blank=True)
    def __str__(self) -> str:
        return self.email
