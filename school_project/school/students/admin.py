from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter  #pip install django-admin-list-filter-dropdown
from .models import Classes, Sections, gr_register, session, class_register, Area, gardian


admin.site.register(Classes)
admin.site.register(Sections)

@admin.register(gr_register)
class gr_registerAdmin(admin.ModelAdmin):
    list_display = ('gr_no', 'first_name', 'last_name', 'date_birth', 'gender', 'classes_C', 'sections_C', 'classes_A')
    #list_filter = ('gender', 'classes')
    list_filter = (
        # for ordinary fields
        ('gender', DropdownFilter),
        # for related fields
        ('classes_C', RelatedDropdownFilter),
    )
    search_fields = ('first_name', 'last_name')
#prepopulated_fields = {'slug': ('title',)}
#raw_id_fields = ('author',)
#date_hierarchy = 'publish'

#admin.site.register(gr_register)

@admin.register(class_register)
class class_registerAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'gr_no', 'class_code', 'section_code', 'session_code')
    #list_filter = ('session_code', 'class_code', 'section_code')
    list_filter = (
        # for ordinary fields
        #('gender', DropdownFilter),
        # for related fields
        ('class_code', RelatedDropdownFilter), ('section_code', RelatedDropdownFilter),
        ('session_code', RelatedDropdownFilter),
    )
    search_fields = ('gr_no',)


#admin.site.register(class_register)
admin.site.register(session)
admin.site.register(Area)
admin.site.register(gardian)
# Register your models here.
