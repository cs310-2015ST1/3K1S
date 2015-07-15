from django.contrib import admin
from liquor_locator.models import LiquorStore, Comment, UserProfile
# Register your models here.

admin.site.register(LiquorStore)
admin.site.register(Comment)
admin.site.register(UserProfile)