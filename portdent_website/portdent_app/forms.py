from django import forms
from portdent_app.models import Client, Post

class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    class Meta:
        model = Client
        fields = "__all__"

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["created_at"]
