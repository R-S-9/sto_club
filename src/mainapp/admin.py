from django.contrib import admin

from .models import (
    ServiceStation,
    ServiceSTO,
    Review,
    Image,
)


class DishInline(admin.TabularInline):
    model = ServiceSTO
    extra = 2


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class STOAdmin(admin.ModelAdmin):
    field = '__all__'

    inlines = [DishInline, ReviewInline, ImageInline]
    list_display = (
        'sto_name',
        'description_sto',
        'location'
    )
    list_filter = ['sto_name']
    search_fields = ['sto_name']


admin.site.register(ServiceStation, STOAdmin)
admin.site.register(Review)
admin.site.register(Image)
admin.site.register(ServiceSTO)
