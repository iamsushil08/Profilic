from django.contrib import admin

# Register your models here.
from .models import About, Skill, Project, Education, Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at', 'is_read')
    list_filter = ('is_read',)

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)