from django.db import models


class Request(models.Model):
    request_id = models.IntegerField(primary_key=True)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
