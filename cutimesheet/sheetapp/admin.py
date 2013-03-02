from django.contrib import admin
from sheetapp.models import Sheet, Week, Day

class DayInline(admin.TabularInline):
    model = Day
    extra = 7

class WeekAdmin(admin.ModelAdmin):
    inlines = [DayInline]

class WeekInline(admin.TabularInline):
    model = Week
    extra = 2

class SheetAdmin(admin.ModelAdmin):
   # admin.site.register(Sheet)
    inlines = [WeekInline]
   # list_filter = [
   #  search_fields = ['submitted']
    date_hierarchy = 'submitted'
admin.site.register(Sheet, SheetAdmin)
admin.site.register(Week, WeekAdmin)




#class DayAdmin(admin.ModelAdmin):
#    fieldsets = [
# see https://docs.djangoproject.com/en/1.5/intro/tutorial02/ to group fields into
# discrete categories
