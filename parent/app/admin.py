from django.contrib import admin

from app.models import ParentSampleModel


@admin.register(ParentSampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    pass
