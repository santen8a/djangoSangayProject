from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    image = forms.FileField()

    

