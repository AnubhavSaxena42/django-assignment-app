from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from user.models import User
from advisor.models import Advisor
from .serializers import BookingSerializer
from user.serializers import UserSerializer
from advisor.serializers import AdvisorSerializer
# Create your views here.

class AdvisorBookingView(APIView):
    def post(self, request, id, a_id):
        time = request.data['time']
        user_id = id
        advisor_id = a_id

        if time is None or time == '':
            return Response(status = status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(id=user_id).first()
        advisor = Advisor.objects.filter(id = advisor_id).first()
        if user is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        if advisor is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        booking_qs = Booking.objects.all()
        for bquery in booking_qs:
            if bquery.advisor_id == advisor_id and bquery.time == time:
                    return Response(status = status.HTTP_400_BAD_REQUEST)
        booking_info = {
            "time": time,
            "user_id":user_id,
            "advisor_id":advisor_id
        }
        serializer = BookingSerializer(data = booking_info)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(status = status.HTTP_200_OK)
    

class RetrieveBookingsView(APIView):
     def get(self, request, id):
        user = User.objects.filter(id=id).first()
        if user is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        booking_qs = Booking.objects.all()
        data_response = []
        for data in booking_qs:
            if data.user_id == id:
                advisor_id = data.advisor_id
                advisor_info = Advisor.objects.filter(id = advisor_id).first()
                booking_info = {
                    "Advisor_name": advisor_info.name,
                    "Advisor_Profile_pic":advisor_info.photo_url,
                    "Advisor_id": advisor_info.id,
                    "Booking_time": data.time,
                    "Booking_id": advisor_info.id,
                }
                data_response.append(booking_info)
        return Response(data_response, status = status.HTTP_200_OK)
       