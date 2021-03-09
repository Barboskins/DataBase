from django.contrib import admin
from phones.models import Phone
class PhonesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phone, PhonesAdmin)
# Register your models here.
