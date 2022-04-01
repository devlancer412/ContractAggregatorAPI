from django.db import models

# Create your models here.
class ContractEvent(models.Model):
    EventId = models.CharField(max_length=30)
    VoterAddress = models.CharField(max_length=70)
    ProposalName = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ContractEvent'