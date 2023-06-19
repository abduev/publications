from django.contrib import admin

from .models import Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('truncated_text', 'author', 'formatted_pub_date')

    def formatted_pub_date(self, obj):
        return obj.pub_date.strftime("%Y-%m-%d %H:%M:%S")

    def truncated_text(self, obj):
        return obj.text[:20] + '...'

    formatted_pub_date.short_description = 'Publication Date'


admin.site.register(Publication, PublicationAdmin)
