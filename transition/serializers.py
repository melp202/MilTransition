from rest_framework import serializers
from .models import State, Organization

# STATE SERIALIZER


class StatesSerializer(serializers.HyperlinkedModelSerializer):
    organizations = serializers.HyperlinkedRelatedField(
        view_name='organization_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = State
        fields = ('id', 'name', 'state_flag', 'organizations')


# ORAGANIZATIONS SERIALIZER
class OrganizationsSerializer(serializers.HyperlinkedModelSerializer):
    state_id = serializers.HyperlinkedRelatedField(
        view_name='state_detail',
        read_only=True
    )

    class Meta:
        model = Organization
        fields = ('state_id', 'name', 'industry', 'image',
                  'description', 'external_link')
