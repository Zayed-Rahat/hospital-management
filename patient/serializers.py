from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Patient
        fields = '__all__'
