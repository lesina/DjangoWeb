from django.db import models
from django.conf import settings
from django.db.models import TextField, DateTimeField, ForeignKey, Model, PositiveIntegerField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    content_type = ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    comments = GenericRelation('comments.Comment', related_name='comments')

    title = models.CharField(max_length = 30, default = "no title")
    text = models.TextField(max_length = 1024)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'person_comment', blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'Comment'
        verbose_name_plural = u'Comments'
        ordering = ('-created_at',)

    def count_likes(self):
        return self.comment_like.count()

    def __str__(self):
        return self.title + " from " + self.author.username
