from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from articleApi.sitemaps import ArticlePostSitemap, CasinoSitemap, GameSupplierSitemap


sitemaps = {
    'article': ArticlePostSitemap,
    'casino': CasinoSitemap,
    'gamesupplier': GameSupplierSitemap
}

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('api/', include('articleApi.urls')),
    path('admin/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", content_type='text/plain')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    re_path(r'^.*',
            TemplateView.as_view(template_name='index.html')),
]
