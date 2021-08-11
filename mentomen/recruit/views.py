from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Comment
from .forms import CommentForm

def home(request):
    return render(request, 'recruit/main.html')

def post(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        postlist = postlist.filter(postname__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'recruit/post.html', {'postlist':postlist, 'q':q})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'recruit/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        new_article=Post.objects.create(
            member=request.POST['member'],
            field=request.POST['field'],
            postname=request.POST['postname'],
            contents=request.POST['contents'],
            pub_date = timezone.now(),
        )
        return redirect('/post/')
    return render(request, 'recruit/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/post/')
    return render(request, 'recruit/remove_post.html', {'Post': post})

def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.co_writer = request.user
            comment.post = post
            comment.save()
            return redirect('/post/' + str(post.id))
    else:
        form = CommentForm()
        return render(request, 'recruit/comment_new.html', {"form":form})

def comment_update(request, comment_id):
    cur_comment = get_object_or_404(Comment, pk=comment_id)
    post = cur_comment.post

    if request.user == cur_comment.co_writer:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance= cur_comment)
            if form.is_valid():
                comment = form.save(commit=False) 
                comment.co_writer = request.user
                comment.save()
                return redirect('/post/' + str(post.id))
        else:
            form = CommentForm(instance=cur_comment)
        return render(request, 'recruit/comment_new.html', {'form': form})
    else:
        return redirect('/post/' + str(cur_comment.post.id))

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.co_writer:
        return redirect('/post/' + str(comment.post.id))
    else:
        comment.delete()
    return redirect('/post/' + str(comment.post.id))