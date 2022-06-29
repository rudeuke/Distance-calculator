from django.db import models


class Request(models.Model):
    request_id = models.TextField(primary_key=True)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()

    def __str__(self):
        timeElapsed = (self.end_timestamp-self.start_timestamp).total_seconds()
        return f'ID: {self.request_id}, TIME ELAPSED: {str(timeElapsed)}'
