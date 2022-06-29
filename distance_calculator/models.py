from django.db import models


class Request(models.Model):
    request_id = models.TextField(primary_key=True)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
