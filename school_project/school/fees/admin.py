from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from .models import concession_type, fees_type, class_fees, fees_source, fee

admin.site.register(concession_type)
admin.site.register(fees_type)
admin.site.register(class_fees)
admin.site.register(fee)
admin.site.register(fees_source)