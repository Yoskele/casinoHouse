from django.contrib import admin

# Register your models here.
from .models import ArticlePost, Casino, GameSupplier

# EXAMPLE  WHAT U CAN DO WITH ADMIN DASHBOARD.
# class ArticlePostAdmin(SummernoteModelAdmin):
#     # exclude = ('slug', )
#     # list_display = ('id', 'title', 'category', 'date_created')
#     # list_display_links = ('id', 'title')
#     # search_fields = ('title', )
#     # list_per_page = 25
#     summernote_fields = ('content', )

admin.site.register(ArticlePost)
admin.site.register(Casino)
admin.site.register(GameSupplier)
