from portdent_app.forms import ContactForm, AddPostForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from portdent_app.models import Client
from django.conf import settings
from django.urls import reverse
from django.contrib.auth. models import User
from django.views.generic import ListView, DetailView, UpdateView
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'portdent_app/index.html')

def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Zapytanie od Klienta"

            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            
            message = "\n".join(body.values())
            
            email = form.cleaned_data['email']
            if not Client.objects.filter(email=email).exists():
                form.save()

            try:
                send_mail(subject, message, 'django_emails@op.pl', ['django_emails@op.pl'])
            except BadHeaderError:
                return HttpResponse("Something went wrong.")
            return redirect('index')

    return render(request, 'portdent_app/contact.html', {'form':form})


class Blog(ListView):
    model = Post
    template_name = 'portdent_app/blog.html'
    
class PostDetails(DetailView):
    model = Post
    template_name = 'portdent_app/details.html'


def map(request):
    key = settings.GOOGLE_API_KEY
    contex = {
        'key':key
    }
    return render(request, 'portdent_app/contact.html', contex)

def addpost(request):
    form = AddPostForm()
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portdent_app:blog'))
        else:
            print(form.errors)
            return HttpResponse("Something went wrong.")
    else:
        return render(request, 'portdent_app/addpost.html', {'form': form})
    

class UpdatePost(UpdateView):
    model = Post
    template_name = 'portdent_app/update_post.html'
    fields = "__all__"