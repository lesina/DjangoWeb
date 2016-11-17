from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=60, label=u'Search', required=False)
    sort = forms.TypedChoiceField(empty_value='-created_at', required=False,
                                  choices=[('-created_at', u'Less'), ('created_at', u'More')],
                                    label=u'Sort')