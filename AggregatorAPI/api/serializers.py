# serializers.py
from rest_framework import serializers

from .models import ContractEvent

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContractEvent
        fields = ('EventId', 'VoterAddress', 'ProposalName')