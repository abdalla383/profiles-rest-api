from django.contrib import admin

from profiles_api import models

# This is registering models in Admin.py to make it accessible through the admin interface
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
