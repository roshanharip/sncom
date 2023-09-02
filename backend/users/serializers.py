from rest_framework import serializers
from  .models import (UserAccount, PharmacyUser, StaffUser, CustomerUser)
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields= '__all__'
    def create(self, clean_data):
        existing_user = UserAccount.objects.filter(email=clean_data['email'])
        if existing_user:
            raise ValidationError(f"User with this email = {clean_data['email']} already exists ")
        if clean_data['is_pharmacy'] == 'True':
                    userObj = UserAccount.objects.create_pharmacy_user(email=clean_data['email'], password=clean_data['password'], name=clean_data['name'], phone_no=clean_data['phone_no'])
        elif clean_data['is_customer'] == 'True':
                    userObj = UserAccount.objects.create_customer_user(email=clean_data['email'], password=clean_data['password'], name=clean_data['name'], phone_no=clean_data['phone_no'])
        elif clean_data['is_staff'] == 'True':
                    userObj = UserAccount.objects.create_staff_user(email=clean_data['email'], password=clean_data['password'], name=clean_data['name'], phone_no=clean_data['phone_no'])
        userObj.save()
        return userObj
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def checkUser(self, clean_data):
        user = authenticate(username=clean_data['email'], password=clean_data['password'])
        if not user:
            raise ValidationError('Invalid credentials')
        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserViewSerializer(serializers.ModelSerializer):
    class Meta :
        model = UserAccount
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = UserAccount
        fields = ['id','name', 'email','is_staff', 'is_pharmacy', 'is_customer']     

class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = '__all__'
    def create(self, clean_data):
        existing_data = CustomerUser.objects.filter(email=clean_data['email'])
        if existing_data:
            raise ValidationError("Customer with the same Email Already Exists")
        try:
            user_obj = CustomerUser.objects.create(email=clean_data['email'], address=clean_data['address'],city=clean_data['city'], gender=clean_data['gender'], date_of_birth=clean_data['date_of_birth'], subscription_start=clean_data['subscription_start'], subscription_expiry=clean_data['subscription_expiry'], subscription_title=clean_data['subscription_title'], customer_id=clean_data['customer_id']) 
            user_obj.save()
            return user_obj
        except:
            raise ValidationError("Saving Problem")
        
class PharmacyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyUser
        fields = '__all__'
    def create(self, clean_data):
        existing_data = PharmacyUser.objects.filter(email=clean_data['email'])
        if existing_data:
            raise ValidationError("Customer with the same Email Already Exists")
        user_obj = PharmacyUser.objects.create(email=clean_data['email'], pharmacy_id=clean_data['pharmacy_id'], is_approved=clean_data['is_approved'], shop_name=clean_data['shop_name'], address=clean_data['address'], city=clean_data['city'], pincode=clean_data['pincode'], district=clean_data['district'], state=clean_data['state'], country=clean_data['country'],contact_person_name=clean_data['contact_person_name'], contact_person_email=clean_data['contact_person_email'], contact_person_phone_no=clean_data['contact_person_phone_no'], license_no=clean_data['license_no'], priority=clean_data['priority'], doc_of_license = clean_data['doc_of_license'], doc_of_ownerId=clean_data['doc_of_ownerId'], doc_of_contactPersonId= clean_data['doc_of_contactPersonId']) 
        user_obj.save()
        return user_obj
    
class StaffUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffUser
        fields = '__all__'
    def create(self, clean_data):
        existing_data = StaffUser.objects.filter(email=clean_data['email'])
        if existing_data:
            raise ValidationError("Customer with the same Email Already Exists")
        user_obj = PharmacyUser.objects.create(email=clean_data['email'], staff_id=clean_data['staff_id'], gender=clean_data['gender'], experience=clean_data['experience'], is_avail=clean_data['is_avail'],address=clean_data['address'], city=clean_data['city'], photo=clean_data['photo'], description=clean_data['description'], document=clean_data['document']) 
        user_obj.save()
        return user_obj