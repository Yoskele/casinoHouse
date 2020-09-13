from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class ArticlePost(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=50)
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='articleImages', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(
            self.slug,
        )

    # # This is for the sitemap.
    def get_absolute_url(self):
        return '/artikel/{}'.format(
            self.slug
        )


class Casino(models.Model):
    slug = models.CharField(max_length=100, unique=True)
    meta_title = models.CharField(max_length=100, blank=True)
    meta_description = models.TextField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True, null=True)
    casinoLogo = models.ImageField(upload_to='casinoLogo', blank=True)
    affiliate_link = models.CharField(max_length=500, blank=True)
    warningLabel = models.CharField(max_length=500, blank=True)
    # For the admin dashboard.

    def __str__(self):
        return(
            self.name
        )

    def get_absolute_url(self):
        return '/recension/{}'.format(
            self.slug
        )


class GameSupplier(models.Model):
    slug = models.CharField(max_length=100, unique=True)
    meta_title = models.CharField(max_length=100, blank=True)
    meta_description = models.TextField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True, null=True)
    gameSupplierLogo = models.ImageField(upload_to='gameSupplier', blank=True)
    # For the admin dashboard.

    def __str__(self):
        return(
            self.name
        )

    def get_absolute_url(self):
        return '/speltillverkare/{}'.format(
            self.slug
        )
