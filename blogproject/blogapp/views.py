from django.shortcuts import render, redirect
from.models import*

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)
def about(request):
    return render(request, '03-About-me.html')
def getPost(request, postId):
    post= Post.objects.get(id=postId)
    return render(request, '02-Single-post.html', {'post': post})
def contact(request):
    return render(request, '04-Contact.html')
def CommingSoon(request):
    return render(request, '05-Comming-soon.html')

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Hi {username}, your account is created successfully!"
            )
            return redirect('nguoidung:index')
    else:
        form = UserRegisterForm()
        messages.error(
            request, "Sorry, there's something wrong with sytem. \nPlease try again in a few seconds."
        )
    return render(request, 'signup.html', {'form':form})

def profine(request):
    return render(request, 'profine.html')
