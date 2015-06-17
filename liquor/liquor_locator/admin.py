from django.contrib import admin
from liquor_locator.models import Category, Page, LiquorStore
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(LiquorStore)
