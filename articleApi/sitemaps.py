from django.contrib.sitemaps import Sitemap

from .models import ArticlePost, Casino, GameSupplier


class ArticlePostSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.5

    def items(self):
        return ArticlePost.objects.all()


class CasinoSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.5

    def items(self):
        return Casino.objects.all()


class GameSupplierSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.5

    def items(self):
        return GameSupplier.objects.all()
