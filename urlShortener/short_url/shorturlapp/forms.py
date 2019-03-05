from django import forms


class ShortUrlForm(forms.Form):
    submit_url = forms.CharField(label='Big Url', max_length=200)
