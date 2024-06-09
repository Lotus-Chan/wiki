from django import forms

class WikiForm(forms.Form):
    title = forms.CharField(label='Wiki Title', max_length=100)
    content = forms.CharField(label='Wiki Content', widget=forms.Textarea)