from rest_framework import serializers
from .models import CreditForm

class CreditFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditForm
        exclude = ['credit_api_response', 'approved']

class CreditFormFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditForm
        fields = '__all__'
