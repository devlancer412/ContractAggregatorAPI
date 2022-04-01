from rest_framework import viewsets

from .serializers import EventSerializer
from .models import ContractEvent

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = ContractEvent.objects.all().order_by('EventId')
    serializer_class = EventSerializer
