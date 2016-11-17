import os
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Video(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(null=True, blank=True)
    video_file = models.FileField(upload_to = u'video/', null = True, blank = False)
    poster = models.FileField(upload_to = u'video/posters/', null = True, blank = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='videos')
    comments = GenericRelation('comments.Comment', related_query_name='comments', verbose_name='Comments')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("video.Category")

    def count_likes(self):
        return self.likes.count()

    def get_comments(self):
        return self.comments

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/video/' + str(self.id)

    def get_edit_url(self):
        return reverse('video:video_edit', args=[str(self.pk)])

    def get_file_url(self):
        return self.photo.url

    class Meta:
        ordering = ('-created_at',)
        verbose_name = u'Video'
        verbose_name_plural = u'Videos'


class Category(models.Model):
    name = models.CharField(max_length = 40, default='SOME STRING')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'

    def get_absolute_url(self):
        return reverse('video:list_category', args=[str(self.short_name)])

    @staticmethod
    def get_categories():
        return [category.name for category in Category.objects.all()]