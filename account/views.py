from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegisterView(APIView):
    def post(self,request,fomate=None):
        data=request.data
        print(data)
        serializers=UserRegisterSerializer(data=data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({"message":"User register successfully"})
        return Response(serializers.errors)

class UserLoginView(APIView):
      def post(self,request,fomat=None):
            serializer = UserLoginSerializer(data=request.data)
            if 'email' not in request.data or 'password' not in request.data:
                return Response({"message": "Both email and password are required fields."},
                            status=status.HTTP_400_BAD_REQUEST)
            if serializer.is_valid():
                  email = serializer.data.get('email')
                  password = serializer.data.get('password')
                  print(email),
                  print(password)
                  user = authenticate(email=email,password=password)
                  token= get_tokens_for_user(user)
                  return  Response({"message":"Login Successful","token":token},status=status.HTTP_200_OK)  
            else:
                  return Response({"message":"Login failed","error":serializer.errors},status=status.HTTP_404_NOT_FOUND) 
            

class DistrictView(APIView):
     def get(self,request,formate=None):
            district_data= [d_choice[0] for d_choice in DISTRICT_CHOICES]
            return Response({'data':district_data},status=status.HTTP_200_OK)
     
class UserCityView(APIView):
     def get(self,request,formate=None):
          city_data=[c_choice[0]for c_choice in CITY_CHOICES]
          return Response({'data':city_data},status=status.HTTP_200_OK)     