from django.db import models


class Execution(models.Model):
    input_file = models.FileField(upload_to='inputs/')
    output_file = models.FileField(upload_to='outputs/', null=True, blank=True)

    input_rows = models.IntegerField(default=0)
    output_rows = models.IntegerField(default=0)

    status = models.CharField(max_length=20, default='UPLOADED')
    created_at = models.DateTimeField(auto_now_add=True)
