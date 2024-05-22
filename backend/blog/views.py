from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from .models import Post, Comment
from .forms import PostForm, CommentForm


def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/feed.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'blog/post.html', {'form': form})


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/post-detail.html', {'post': post, 'form': form})


def comment():
    pass