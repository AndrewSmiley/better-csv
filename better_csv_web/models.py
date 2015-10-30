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
    master_file= models.ForeignKey(File, null=False, related_name='master_file')
    source_file= models.ForeignKey(File, null=False,related_name='source_file')
    def __unicode__(self):
        return "%s %s" % (self.source_file.filename, str(self.source_column_id) if self.source_column_name == "N/A" else self.source_column_name)

class SearchColumn(models.Model):
    column_id = models.IntegerField()
    file = models.ForeignKey(File, null=False)
    column_name = models.CharField(max_length=70, default="N/A")
    def __unicode__(self):
        return "%s %s" % (self.file.filename, self.column_id if self.column_name == "N/A" else self.column_name)

class Folder(models.Model):
    folder_name = models.CharField(max_length=70, null=False)
    def __unicode__(self):
        return self.folder_name

class Action(models.Model):
    action_name=models.CharField(max_length=50)
    code = models.CharField(max_length=250)

    def __unicode__(self):
        return self.action_name


class MacroColumn(models.Model):
    macro_column_name = models.CharField(max_length=50)
    file_reference = models.ForeignKey(File, null=False)
    column_id = models.IntegerField(null=False)

    def __unicode__(self):
        return self.macro_column_name

class Macro(models.Model):
    macro_name = models.CharField(max_length=50)
    action = models.ForeignKey(Action, null=False)
    # arguments = models.ManyToManyField(MacroColumn,null=False)
    master_file = models.ForeignKey(File, null=False)
    master_file_column_id = models.IntegerField(null=False)
    source_file_columns = models.ManyToManyField
    def __unicode__(self):
        return self.macro_name

