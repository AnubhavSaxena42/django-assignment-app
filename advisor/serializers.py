from rest_framework import serializers
from .models import Advisor

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ['name', 'photo_url']