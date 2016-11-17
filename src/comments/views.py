from django.shortcuts import render, reverse
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from .models import Comment
from .forms import CommentForm


class PostComment(CreateView):
    form_class = CommentForm
    template_name = "video:video_detail"

    # def dispatch(self, request, pk = None, *args, **kwargs):
    #     self.post = get_object_or_404(Video, id=pk)
    #     return super(PostComment, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostComment, self).get_context_data(**kwargs)
        context['post'] = self.post
        context['form'] = CommentForm
        return context