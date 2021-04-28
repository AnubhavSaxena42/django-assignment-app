from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdvisorSerializer
from user.serializers import UserSerializer
from bookings.serializers import BookingSerializer
from .models import Advisor
from user.models import User
from bookings.models import Booking
 # Create your views here.
class AdvisorRegistrationView(APIView):
    def post(self, request):
        name = request.data['name']
        photo_url = request.data['photo_url']
        if photo_url is None or photo_url == '':
            return Response(status = status.HTTP_400_BAD_REQUEST)
        if name is None or name == '':
            return Response(status = status.HTTP_400_BAD_REQUEST)

        serializer = AdvisorSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(status = status.HTTP_200_OK)  
    
class RetrieveAdvisorView(APIView):
    def get(self, request, id):
        user = User.objects.filter(id=id).first()
        if user is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            advisors = Advisor.objects.all()
            json_response = []
            for each in advisors:
                js_advisor = {
                    "Advisor_name": each.name,
                    "Advisor_Profile_pic":each.photo_url,
                    "Advisor_id": each.id
                }
                json_response.append(js_advisor)
            return Response(json_response)
      
 
