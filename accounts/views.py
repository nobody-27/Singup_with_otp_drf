from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializer import UserSerializer,VerifyAccountSerializer,User_Document_Serializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from rest_framework.parsers import FormParser, MultiPartParser
from accounts.emails import (
    send_email_via_email
)
# Create your views here.

class RegisterApi(APIView): 
    permission_classes = [AllowAny,]

    def post(self,request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if  serializer.is_valid():
                serializer.save()
                send_email_via_email(serializer.data['email'])
                return Response({
                    'status':200,
                    'message':'resgiter...',
                    'data':serializer.data
                })
            
            return Response({
                'status':400,
                'message':serializer.errors
            })
        except Exception as e:
            print(e)


class Verify_Otp(APIView):
    permission_classes = [AllowAny,]
    serializer_class = VerifyAccountSerializer
    def post(self,request):
        try:

            serializer = VerifyAccountSerializer(data=request.data)

            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                

                user = User.objects.filter(email=email)

                print(user[0].is_verified,"Value")

                if user[0].is_verified == True:
                    return Response({
                        'status':200,
                        'message':'user already verifyed',
                        'data':'user already verifyed'
                })


                if not user.exists():
                    return Response({
                        'status':400,
                        'message':'someting went wrong',
                        'data':'invalid email'
                })

                
                
                if not user[0].otp == otp:
                    return Response({
                        'status':400,
                        'message':'YOU HAVE ENTER WRONG OTP',
                        'data':'WRONG OTP'
                })
                

                user.update(is_verified = True)
                print(user[0].is_verified,"make verify")

                return Response({
                    'status':200,
                    'message':'Account Verify',
                    'data':serializer.data
                })

        except Exception as e:
            print(e)
            return Response({
                'status':400,
                'message':'Someting Went Wrong',
            })


class Upload_Docs(APIView):
    permission_classes = [AllowAny,]
    serializer_class = User_Document_Serializer
    # parser_classes = (FormParser, MultiPartParser)
    def post(self,request):

        data = request.data
        try:
            print(data.document,"document path....")
        except Exception as e:
            pass

        serializer = User_Document_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            docs = serializer.data['document']
            print(docs,"THIS IS DOCUMENTS....")
            return Response({
                'message':serializer.data,
            })
