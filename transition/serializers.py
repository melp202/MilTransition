from rest_framework import serializers
from .models import State, Organization

#STATE SERIALIZER
class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


# ORAGANIZATIONS SERIALIZER
class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'