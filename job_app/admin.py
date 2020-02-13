from django.contrib import admin
from django.contrib import admin
from job_app.models import Jobs,Category

# Register your models here.


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ("title", "location","company_name","company_description","created_at")
    prepopulated_fields = {"slug": ("title",)}
    # readonly_fields = ("author",)
    # 
    # 
admin.site.register(Category)

# Register your models here.
