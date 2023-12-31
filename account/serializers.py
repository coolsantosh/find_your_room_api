from rest_framework import serializers
from .models import *


# class UserRegisterSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(write_only=True) 
#     class Meta:
#         model=User
#         fields=['email','name','address','mobile','city','district','password','password2']
#         extra_kwargs={
#             'password':{'write_only':True}
#         }

#     def validate(self, attrs):
#         password=attrs.get('password')
#         password2=attrs.get('password2')
#         if password != password2:
#          return serializers.ValidationError("Password and confirm password don't match")
#         return attrs
    
#     # def create(self, validate_data):
#     #     return User.objects.create_user(**validate_data)


class UserRegisterSerializer(serializers.ModelSerializer):
     password2=serializers.CharField(style={'input_type':'password'},write_only=True)
     class Meta:
        model = User
        fields=['email','name','address','mobile','city','district','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }


     def validate(self, attrs):
        
         password=attrs.get('password')
         password2 = attrs.get('password2')
         if password != password2:
          raise serializers.ValidationError('password and confirm password does not match')
         return attrs

     def create(self, validated_data):
        return User.objects.create_user(**validated_data)  


class UserLoginSerializer(serializers.ModelSerializer):
   email = serializers.EmailField(max_length=255)
   class Meta:
      model= User
      fields= ['email','password']
