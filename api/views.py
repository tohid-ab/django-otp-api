from .permission import *
from .serializers import *
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from accounts.models import PhoneNumberUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class OTPView(APIView):
    def get(self, request):
        serializer = RequestOTPSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                otp = OTPRequest.objects.generate(data)
                return Response(data=RequestOTPSerializer(otp).data)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def post(self, request):
        serializer = VerifyOtpRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if OTPRequest.objects.is_valid(data['receiver'], data['request_id'], data['password']):
                return Response(self._handle_login(data))
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def _handle_login(self, otp):
        User = get_user_model()
        query = User.objects.filter(username='UsAhjbsd'+otp['receiver']+'ApW')
        if query.exists():
            created = False
            user = query.first()
        else:
            user = User.objects.create(username='UsAhjbsd'+otp['receiver']+'ApW')
            created = True

        token = Token.objects.create(user=user)

        return ObtainTokenSerializer({
            'token': str(token.key),
            'request_id': str(user.id),
            'username': str(user.username),
            'phone': str(otp['receiver']),
            'created': created
        }).data
