from django.shortcuts import render, redirect, get_object_or_404
from django.conf.urls import url, include
from . models import Post, Comment
from . form import CommentForm

def list_of_comment(request, pk):
    comment = Comment.objects.all()
    template = 'blog/comment.html'
    context = {'comment':comment}
    return render(request, template, context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    template = 'blog/post.html'
    context = {'post':post}
    return render(request, template, context)
    
    

# Create your views here.

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    template = 'blog/comment.html'
    context = {'form': form}
    return render(request, template, context)
            
