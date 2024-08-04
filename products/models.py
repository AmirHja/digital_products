from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                               verbose_name=_('parent'))
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(verbose_name=_('avatar'), upload_to='categories/images/', blank=True)
    is_enabled = models.BooleanField(verbose_name=_('is enabled'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ['title']
        indexes = [models.Index(fields=['title']), models.Index(fields=['is_enabled'])]


class Product(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=100)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(verbose_name=_('avatar'), upload_to='products/images/', blank=True)
    is_enabled = models.BooleanField(verbose_name=_('is enabled'), default=True)
    category = models.ManyToManyField(Category, verbose_name=_('category'), blank=True)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ['-created_time']
        indexes = [models.Index(fields=['title']), models.Index(fields=['-created_time'])]


class File(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('product'), related_name='files')
    title = models.CharField(verbose_name=_('title'), max_length=100)
    file = models.FileField(verbose_name=_('file'), upload_to='files/%Y/%m/%d/', blank=True)
    is_enabled = models.BooleanField(verbose_name=_('is enabled'), default=True)
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')
        ordering = ['-created_time']
        indexes = [models.Index(fields=['title']), models.Index(fields=['-created_time'])]


