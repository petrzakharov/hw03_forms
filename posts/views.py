from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


@login_required
def new_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form_instance_updated = form.save(commit=False)
        form_instance_updated.author = request.user
        form_instance_updated.save()
        return redirect("index")
    return render(request, "new.html", {"form": form})
