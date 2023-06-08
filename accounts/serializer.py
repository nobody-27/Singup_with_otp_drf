from rest_framework import serializers
from .models import User,File_Form

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','is_verified']



class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()


class User_Document_Serializer(serializers.ModelSerializer):
    class Meta:
        model = File_Form
        fields = ['document']
    

