from django.contrib import admin
from .models import Notification


# Admin display
class NotificationAdmin(admin.ModelAdmin):
    list_filter = ["title","timeModified","read"]
    list_display = ["title", "timeModified","read"]

admin.site.register(Notification, NotificationAdmin)