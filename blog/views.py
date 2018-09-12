from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import PostForm, UserForm


# Create your views here.
def globalContext(request, context):
    context['base_template'] = "base_template.html"
    return


def index(request):
    context = { "title": "Blog" }
    globalContext(request, context)

    posts = Post.objects.all()
    context["posts"] = posts

    return render(request, 'index.html', context)


def sign_up(request):
    context = { "title": "Sign Up" }
    globalContext(request, context)

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(username, None, password)
            user.save()


    form = UserForm()

    context["form"] = form
    return render(request, 'sign_up.html', context)


def log_in(request):
    context = {"title": "Log In"}
    globalContext(request, context)

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

    return render(request, 'sign_up.html', context)


def create_post(request):
    context = { "title": "Create Post" }
    globalContext(request, context)

    print(context)

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():



            post = Post(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
                pub_date=datetime.now()
            )

            post.save()

            print(post)




    else:
        form = PostForm()

    context["form"] = form

    return render(request, 'create_post.html', context)
