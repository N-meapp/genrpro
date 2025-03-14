from django.contrib import admin
from .models import *
from genrapp.models import JobApplication,ContactForm



# Register your models here.


admin.site.register(Our_Products)
admin.site.register(Gallery)
admin.site.register(Offer)
admin.site.register(Enquiry)
admin.site.register(Career)
admin.site.register(JobApplication)
# admin.site.register(ContactForm)
admin.site.register(News)
admin.site.register(Login)
admin.site.register(Count)

class Additional_imagesTabular(admin.TabularInline):
    model = Addiotional_work_images

class WorkAdmin(admin.ModelAdmin):
    inlines = [Additional_imagesTabular]

admin.site.register(Our_Works, WorkAdmin)

admin.site.site_header = "GEN-R"

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'enquiry_type', 'submitted_at')
    search_fields = ('name', 'email', 'enquiry_type')
    list_filter = ('enquiry_type', 'submitted_at')