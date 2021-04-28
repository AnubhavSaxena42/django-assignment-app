from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
import jwt,datetime

class UserRegistrationView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        name = request.data['name']
        if email is None or email == '':
            return Response(status = status.HTTP_400_BAD_REQUEST)
        if password is None or password == '':
            return Response(status = status.HTTP_400_BAD_REQUEST)
        if name is None or name == '':
            return Response(status = status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        user = User.objects.filter(email=email).first()        

        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat':datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response({'JWT Authentication Token': token, 'User id':user.id}, status = status.HTTP_200_OK)        


class UserLoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        if email is None or email == '':
            return Response(status = status.HTTP_400_BAD_REQUEST)
        if password is None or password == '':
            return Response(status = status.HTTP_400_BAD_REQUEST)


        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        if not user.check_password(password):
            return Response(status = status.HTTP_401_UNAUTHORIZED)

        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat':datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response({'JWT Authentication Token': token, 'User id':user.id}, status = status.HTTP_200_OK)


