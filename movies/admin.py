from django.contrib import admin
from .models import Movies, Cast, Category, review, IdNumber
# Register your models here.


class MoviesAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    search_fields = ('name','actors__the_hero_name')
    list_display = ('name', 'likes', 'watch_count', 'rate', 'Custom_column')
    readonly_fields = ('Custom_column',)
    def Custom_column(self, obj):
        return 'Good'

    fieldsets = (
        ["section A", {"fields":["name", "description"]}],
    [None, {"fields":["likes", "watch_count", "rate", "Custom_column"]}],
        ["upload files",{"fields":["poster","video"]}],
        ["actors",{"fields":["actors"]}]

    )
















admin.site.register(Movies, MoviesAdmin)
admin.site.register(Cast)
admin.site.register(Category)
admin.site.register(review)
admin.site.register(IdNumber)