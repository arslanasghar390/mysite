from django.contrib import admin


# Register your models here.
from myapp.models import Contact, upload

admin.site.register(Contact)
admin.site.register(upload)