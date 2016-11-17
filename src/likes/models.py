from django.db import models
from django.conf import settings


class Like(models.Model):

    video = models.ForeignKey("video.Video", related_name = 'likes')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'person_likes')

    def __str__(self):
        return self.video.title

    class Meta:
        verbose_name = u'Like'
        verbose_name_plural = u'Likes'


class CommentLike(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='person_comment_likes', default = 0)
    comment = models.ForeignKey("comments.Comment", related_name = 'comment_like', default = 0)

    def __str__(self):
        return self.comment.title

    class Meta:
        verbose_name = u'Comment like'
        verbose_name_plural = u'Comment likes'