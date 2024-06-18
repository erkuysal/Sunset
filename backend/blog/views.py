from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from .models import Post, Like
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
            print(form.errors)  # Add this line to see validation errors
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


@login_required
def like_post(request, post_id):
    # post = get_object_or_404(Post, id=post_id)
    # like, created = Like.objects.get_or_create(user=request.user, post=post)
    # if not created:
    #     like.delete()
    # return redirect(request.META.get('HTTP_REFERER', 'post_list'))
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    like_count = post.total_likes
    return JsonResponse({'liked': liked, 'like_count': like_count, 'post_id': post_id})

