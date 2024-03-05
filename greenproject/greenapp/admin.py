from django.contrib import admin
from .models import CustomUser, Volunteer, News,SubscribedUsers, Contact


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Volunteer)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(SubscribedUsers, SubscribedUsersAdmin)