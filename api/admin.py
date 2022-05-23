from django.contrib import admin
from .models import Tasks, Employers
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Tasks)
class tasksxls(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass

@admin.register(Employers)
class employersxls(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
    pass