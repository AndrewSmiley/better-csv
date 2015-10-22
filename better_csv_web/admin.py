__author__ = 'pridemai'
from django.contrib import admin
from better_csv_web.models import File,ColumnMapping,SearchColumn,Folder

admin.site.register(File)
admin.site.register(ColumnMapping)
admin.site.register(SearchColumn)
admin.site.register(Folder)