from django.contrib import admin
from .models import (
  DemoRequest, 
  Stats, 
  ChartData, 
  Card,
  Plan,
  PlanFeature,
  ContactInfo,
)

@admin.register(DemoRequest)
class DemoRequestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone_number')
    list_filter = ('created_at',)


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'percent', 'updated_at', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active', 'updated_at')

@admin.register(ChartData)
class ChartDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'chart_style', 'updated_at')
    search_fields = ('title',)
    list_filter = ('chart_style', 'updated_at')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'order', 'is_active')
    search_fields = ('title', 'section')
    list_filter = ('section', 'is_active')

class PlanFeatureInline(admin.TabularInline):
    model = PlanFeature
    extra = 1

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_popular', 'order', 'is_active')
    list_editable = ('is_popular', 'order', 'is_active')
    inlines = [PlanFeatureInline]

@admin.register(PlanFeature)
class PlanFeatureAdmin(admin.ModelAdmin):
    list_display = ('plan', 'text')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if ContactInfo.objects.exists():
            return False
        return True