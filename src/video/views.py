from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, reverse, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import redirect_to_login
from django.db.models import Q

from application.settings import LOGIN_URL
from .models import Video, Category
from comments.models import Comment
from comments.forms import CommentForm
from .forms import SearchForm


class VideoList(ListView):
    template_name = "video/video_list.html"
    model = Video
    context_object_name = 'video_list'
    paginate_by = 20

    def dispatch(self, request, *args, **kwargs):
        self.search_form = SearchForm(request.GET)
        return super(VideoList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Video.objects.all()
        if self.search_form.is_valid():
            query = self.search_form.cleaned_data['search']
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query))
            queryset = queryset.order_by(self.search_form.cleaned_data['sort'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(VideoList, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form
        context['categories'] = Category.get_categories()
        context['carousel'] = Video.objects.all().order_by('-created_at')[:3]
        return context


class VideoCategoryView(VideoList):
    slug_field = 'category'

    def dispatch(self, request, *args, **kwargs):
        self.category = kwargs['slug']
        return super(VideoCategoryView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(VideoCategoryView, self).get_queryset()
        if self.category == 'all':
            return queryset
        return queryset.filter(category__name=self.category)


class VideoDetail(DetailView):
    model = Video
    template_name = 'video/video.html'
    success_url = "."

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.comment_form = CommentForm
        return super(VideoDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(VideoDetail, self).get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.comment_form(request.POST)
        if request.user.is_anonymous():
            return redirect_to_login(next=reverse('video:video_detail', args=[str(self.object.pk)]), login_url=LOGIN_URL)
        if form.is_valid():
            comment = Comment()
            comment.author = request.user
            comment.text = form.cleaned_data['comment']
            comment.content_type = ContentType.objects.get_for_model(self.model)
            comment.object_id = self.object.pk
            comment.save()
        return HttpResponseRedirect(self.success_url)

class CreateVideo(CreateView):
    model = Video
    template_name = 'video/create_video.html'
    fields = ('title', 'video_file', "poster", 'description', 'category')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateVideo, self).form_valid(form)

    def get_success_url(self):
        return reverse('video:video_detail', args=[str(self.object.pk)])


class EditVideo(UpdateView):
    model = Video
    template_name = 'video/video_edit.html'
    fields = ('title', 'poster', 'description', 'category')

    def get_queryset(self):
        return Video.objects.filter(author=self.request.user)
