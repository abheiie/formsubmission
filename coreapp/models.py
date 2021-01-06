from django.db import models
from django.utils import timezone


# Create your models here.
class WebhookTransaction(models.Model):
    UNPROCESSED = 1
    PROCESSED = 2
    ERROR = 3

    STATUSES = (
        (UNPROCESSED, 'Unprocessed'),
        (PROCESSED, 'Processed'),
        (ERROR, 'Error'),
    )

    date_generated = models.DateTimeField()
    date_received = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')
    request_meta = models.TextField(default='')
    status = models.CharField(max_length=250, choices=STATUSES, default=UNPROCESSED)

    def unicode(self):
        return u'{0}'.format(self.date_generated)
    
    class Meta:
        db_table = "data_gather_webhooktransaction"

class ActivityManagement(models.Model):
    date_processed = models.DateTimeField(default=timezone.now)
    webhook_transaction = models.OneToOneField(WebhookTransaction,on_delete=models.DO_NOTHING)

    activity = models.CharField(max_length=20)
    id_number = models.CharField(max_length=10)
    agent_id_number = models.CharField(max_length=10)
    def unicode(self):
        return u'{}'.format(self.agent_id_number)

    class Meta:
        db_table = "data_gather_activitymanagement"


class FormSubmission(models.Model):
    date_processed = models.DateTimeField(default=timezone.now)
    webhook_transaction = models.OneToOneField(WebhookTransaction,on_delete=models.DO_NOTHING)
    agent_id_number = models.CharField(max_length=10)
    def unicode(self):
        return u'{}'.format(self.agent_id_number)

    class Meta:
        db_table = "data_gather_formsubmission"
    