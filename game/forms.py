from django import forms


class WordForm(forms.Form):
    user_entry = forms.CharField(max_length=400)
