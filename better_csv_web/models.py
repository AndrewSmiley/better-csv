__author__ = 'pridemai'
from django.db import models


class File(models.Model):
    filename = models.CharField(max_length=75, null=False)
    is_master = models.BooleanField(default=False)
    def __unicode__(self):
        return self.filename
class ColumnMapping(models.Model):
    master_column_id = models.IntegerField(null=False)
    master_column_name = models.CharField(max_length=70, default="N/A")
    source_column_id = models.IntegerField(null=False)
    source_column_name = models.CharField(max_length=70, default="N/A")
    file_id = models.ForeignKey(File, null=False)
    def __unicode__(self):
        return self.master_column_name if self.master_column_name != "N/A" else str(self.master_column_id)

