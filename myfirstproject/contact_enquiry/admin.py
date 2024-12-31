from django.contrib import admin
from contact_enquiry.models import Contact
class contactadmin(admin.ModelAdmin):
    list_display=("contact_name","contact_email","contact_phone","contact_message")
admin.site.register(Contact,contactadmin)

# Register your models here.
