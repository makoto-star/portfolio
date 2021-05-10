from django.contrib import admin

from .models import Profile, Description, Skill, Work, Carrer
# Register your models here.


admin.site.register(Profile)
admin.site.register(Description)
admin.site.register(Skill)
admin.site.register(Work)
admin.site.register(Carrer)