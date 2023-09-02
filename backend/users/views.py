from .models import UserAccount
from django.contrib.auth import login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserLoginSerializer,ChangePasswordSerializer, UserRegisterSerializer, CustomerUserSerializer, PharmacyUserSerializer, StaffUserSerializer
from rest_framework import permissions, status
from .validation import (custom_validation, validate_email, validate_password)
from rest_framework.decorators import api_view
from  .models import (UserAccount, PharmacyUser, StaffUser, CustomerUser)


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	
	def post(self, request):
		data = request.data
		assert validate_email(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data) 
		if serializer.is_valid(raise_exception=True):
			user = serializer.checkUser(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class ChangePassword(APIView):
    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            if not user.check_password(old_password):
                return Response({'detail': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)

	def get(self, request):
		serializer = UserSerializer(request.user)
		email = serializer.data["email"]
		cUser = serializer.data['is_customer']
		pUser = serializer.data['is_pharmacy']
		sUser = serializer.data['is_staff']
		if cUser:
			model = CustomerUser.objects.filter(email=email)
			if model:
				cSerializer = CustomerUserSerializer(model,many=True)
				return Response({'user': serializer.data, 'details': cSerializer.data}, status=status.HTTP_200_OK)
			else:
				return Response({'user': serializer.data, }, status=status.HTTP_200_OK)
		elif pUser:
			model = PharmacyUser.objects.filter(email=email)
			if model:
				pSerializer = PharmacyUserSerializer(model, many=True)
				return Response({'user': serializer.data, 'details': pSerializer.data}, status=status.HTTP_200_OK)
			else:
				return Response({'user': serializer.data, }, status=status.HTTP_200_OK)
				
		elif sUser:
			model = StaffUser.objects.filter(email=email)
			if model:
				sSerializer = StaffUserSerializer(model, many=True)
				return Response({'user': serializer.data, 'details': sSerializer.data}, status=status.HTTP_200_OK)
			else:
				return Response({'user': serializer.data, }, status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def post(self,request):
		serializer = UserSerializer(request.user)
		cUser = serializer.data['is_customer']
		pUser = serializer.data['is_pharmacy']
		sUser = serializer.data['is_staff']
		clean_data = request.data
		clean_data['email'] = serializer.data['email']
		if cUser:
			customerSerializer = CustomerUserSerializer(data=clean_data)
			if customerSerializer.is_valid(raise_exception=True):
				obj = customerSerializer.create(clean_data)
				if obj:
					return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
		elif pUser:
			pharmacySerializer = PharmacyUserSerializer(data=clean_data)
			if pharmacySerializer.is_valid(raise_exception=True):
				obj = pharmacySerializer.create(clean_data)
				if obj:
					return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
		elif sUser:
			staffSerializer = StaffUserSerializer(data=clean_data)
			if staffSerializer.is_valid(raise_exception=True):
				obj = staffSerializer.create(clean_data)
				if obj:
					return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
            
            
 
# class UserViewCheck(APIView):
    
	# permission_classes = (permissions.IsAuthenticated,)
	# authentication_classes = (SessionAuthentication,)
	# def get(self, request):
	# 	user = UserSerializer(request.user)
	# 	email = user.data["email"]
	# 	model = CustomerUser.objects.filter(email=email)
	# 	serializer = CustomerUserSerializer(model, many=True)
  
	# 	return Response({'user': serializer.data, }, status=status.HTTP_200_OK)


