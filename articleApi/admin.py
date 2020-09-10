from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import ArticlePost, Casino, GameSupplier


class ArticlePostAdmin(SummernoteModelAdmin):
    # exclude = ('slug', )
    #   list_display = ('id', 'title', 'category', 'date_created')
    # list_display_links = ('id', 'title')
    # search_fields = ('title', )
    # list_per_page = 25
    summernote_fields = ('content', )


class CasinoAdmin(SummernoteModelAdmin):
    # exclude = ('slug', )
    #   list_display = ('id', 'title', 'category', 'date_created')
    # list_display_links = ('id', 'title')
    # search_fields = ('title', )
    # list_per_page = 25
    summernote_fields = ('content', )


class GameSupplierAdmin(SummernoteModelAdmin):
    # exclude = ('slug', )
    #   list_display = ('id', 'title', 'category', 'date_created')
    # list_display_links = ('id', 'title')
    # search_fields = ('title', )
    # list_per_page = 25
    summernote_fields = ('content', )


admin.site.register(ArticlePost, ArticlePostAdmin)
admin.site.register(Casino, CasinoAdmin)
admin.site.register(GameSupplier, GameSupplierAdmin)
