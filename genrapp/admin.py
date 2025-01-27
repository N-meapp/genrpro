from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Our_Products)
admin.site.register(Gallery)
admin.site.register(Offer)
admin.site.register(Enquiry)
admin.site.register(Career)
admin.site.register(News)
admin.site.register(Login)

class Additional_imagesTabular(admin.TabularInline):
    model = Addiotional_work_images

class WorkAdmin(admin.ModelAdmin):
    inlines = [Additional_imagesTabular]

admin.site.register(Our_Works, WorkAdmin)

admin.site.site_header = "GEN-R"
