from django.contrib import admin

from .models import Profile, FamilyMember, Education

admin.site.register(Profile)
admin.site.register(FamilyMember)
admin.site.register(Education)