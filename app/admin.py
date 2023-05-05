from django.contrib import admin
# Register your models here.
from .models import *


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ("email", "name")

admin.site.register(ArtistInformation)
admin.site.register(Post)
admin.site.register(Url)
admin.site.register(SubscribedUsers, SubscribedUsersAdmin)



