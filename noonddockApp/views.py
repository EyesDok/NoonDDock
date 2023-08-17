from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from noonddockApp.models import Post, Like, Comment
from django.http import JsonResponse

# Create your views here.

#눈똑 게시글 리스트
def post_list_view(request):

    #추천수 기준 내림차순 정렬 상위 12개 게시물
    post_list = Post.objects.all().order_by('-like_count')[:12]
    
    #게시글 작성일 기준 내림차순 정렬 (선택)'최신순'
    if request.GET.get('order') == 'recent':        
        post_list = Post.objects.all().order_by('-pub_date') 

    #게시글 추천수 기준 내림차순 정렬 (선택) '인기순'
    elif request.GET.get('order') == 'popular':
        post_list = Post.objects.all().order_by('-like_count')

    #게시글 등산/낚시 기준 내림차순 정렬 (선택) '등산/낚시'
    elif request.GET.get('order') == '1':
        post_list = Post.objects.all().order_by('-category')

    #게시글 공연/콘서트 기준 내림차순 정렬 (선택) '공연/콘서트'
    elif request.GET.get('order') == '2':
        post_list = Post.objects.all().order_by('-category')

    #게시글 연극/뮤지컬 기준 내림차순 정렬 (선택) '연극/뮤지컬'
    elif request.GET.get('order') == '3':
        post_list = Post.objects.all().order_by('-category')

    #게시글 스포츠/레저 기준 내림차순 정렬 (선택) '스포츠/레저'
    elif request.GET.get('order') == '4':
        post_list = Post.objects.all().order_by('-category')

    #게시글 전시/행사 기준 내림차순 정렬 (선택) '전시/행사'
    elif request.GET.get('order') == '5':
        post_list = Post.objects.all().order_by('-category')

    #게시글 서울/경기/인천 기준 내림차순 정렬 (선택) '서울/경기/인천'
    elif request.GET.get('order') == '1':
        post_list = Post.objects.all().order_by('-city_cate')

    #게시글 강원/강릉/원주 기준 내림차순 정렬 (선택) '강원/강릉/원주'
    elif request.GET.get('order') == '2':
        post_list = Post.objects.all().order_by('-city_cate')

    #게시글 세종/충남/충북/대전 기준 내림차순 정렬 (선택) '세종/충남/충북/대전'
    elif request.GET.get('order') == '3':
        post_list = Post.objects.all().order_by('-city_cate')

    #게시글 부산/울산/경남/경북 기준 내림차순 정렬 (선택) '부산/울산/경남/경북'
    elif request.GET.get('order') == '4':
        post_list = Post.objects.all().order_by('-city_cate')

    #게시글 광주/전남/전북 기준 내림차순 정렬 (선택) '광주/전남/전북'
    elif request.GET.get('order') == '5':
        post_list = Post.objects.all().order_by('-city_cate')

    #게시글 제주 기준 내림차순 정렬 (선택) '제주'
    elif request.GET.get('order') == '6':
        post_list = Post.objects.all().order_by('-city_cate')
        
    else:
        post_list = Post.objects.all()
    if request.user.is_authenticated:
        for post in post_list:
            post.is_recommened = post.like_set.filter(user=request.user).exists()

    context ={
            'post_list': post_list,
        }
    
    return render(request, 'NoonDDocklistPage/post_list.html', context)


#좋아요 기능=눈똑수
@login_required
def liked_post(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(post, id=id)
        user = request.user

        if request.user in post.like_users.all():
            post.like_users.remove(request.user)
            post.like_count -= 1
        else:
            post.like_users.add(request.user)
            post.like_count += 1

        post.save()

        return redirect('NoonDDocklistPage/post_list.html')

    return redirect('accouts/login.html')
    

#js 토글 관련, js 잘 몰라서 그냥 냅두는 중
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    like, created = Like.objects.get_or_create(user=user, post=post)
    
    if not created:
        like.delete()
    
    like_count = post.like_set.count()
    liked = created
    
    return JsonResponse({'liked': liked, 'like_count': like_count})

#눈똑 상세 페이지
def post_inform(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    context = {
        'post': post,
    }
    
    return render(request, 'InformPage/Inform.html', context)

#메인 페이지
def main(request):
    post_list = Post.objects.all()[:4]

    if request.user.is_authenticated:
        user_liked = Like.objects.filter(user=request.user)
        for post in post_list:
            post.is_liked = user_liked.filter(post=post).exists()

    context = {
        'post_list' : post_list,
    }
    return render(request, 'MainPage/main.html', context)

#눈똑 페이지
def noonddock(request):
    post_list = Post.objects.all().order_by('-pub_date')[:3]

    if request.user.is_authenticated:
        user_liked = Like.objects.filter(user=request.user)
        for post in post_list:
            post.is_liked = user_liked.filter(post=post).exists()

    context = {
        'post_list' : post_list,
    }
    return render(request, 'NoonDDockPage/NoonDDock.html', context)

#나의 눈똑 페이지
def my_noonddock(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/login.html')  # 로그인 페이지로 이동 또는 처리

    liked_posts = Post.objects.filter(like_users=request.user)

    context = {
        'liked_posts': liked_posts,
    }


    return render(request, 'MyNoonDDockPage/my_noonddock.html', context)


from django.http import JsonResponse

def update_like_count(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id')
        action = request.GET.get('action')

        try:
            post = Post.objects.get(id=post_id)
            if action == 'add':
                post.like_count += 1
            elif action == 'remove':
                post.like_count -= 1
            post.save()
            
            return JsonResponse({'success': True})
        except Post.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Post not found'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def comment_create(request):
    # POST 요청 시
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # 시니어/자녀 정보 받아오기
        membership = request.POST.get('membership')

        # DB에 유저 추가
        comment = Comment.objects.create(username=username, email=email, password=password1, membership=membership)
        comment.save()

        # 회원가입 성공 시 로그인 페이지로 이동
        return redirect('accounts:login')
    # GET 요청 시
    return render(request, 'accounts/signup.html')