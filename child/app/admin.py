from django.contrib import admin

from app.models import ChildSampleModel


@admin.register(ChildSampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    pass

