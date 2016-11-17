from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=1024, widget=forms.Textarea, label='Comment')

    def clean_text(self):
        text = self.cleaned_data['comment']
        if text.isspace():
            raise forms.ValidationError(u'Empty string!')

    class Meta:
        model = Comment
        fields = ('comment', )