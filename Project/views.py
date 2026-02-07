from django.shortcuts import render,redirect,get_object_or_404
from .form import UserForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import  login,logout
from .models import BlogPost,Category
from .form import CommentForm,BlogForm,ProfileForm
from django.core.paginator import Paginator


# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserForm()
        
    return render(request,'register.html',{'form':form})






def home(request):
    q = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')
    posts = BlogPost.objects.all()
    categories = Category.objects.all()

    if q:
        posts = posts.filter(title__icontains=q)
    elif category_filter:
        posts = posts.filter(category__name__icontains=category_filter)

    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'posts': page_obj,
        'q': q,
        'categories': categories,
        'category_filter': category_filter
    })


def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})







def Logout(request):
    logout(request)
    return redirect('login')






def detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("detail", slug=post.slug)  # refresh page after comment
    else:
        form = CommentForm()

    return render(request, "detail.html", {"post": post, "form": form})




def create_post(request):
    user=request.user
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=user
            post.save()
            return redirect('home')
    else:
        form=BlogForm()
        
    return render(request,'create_post.html',{'form':form})









def profile(request):
    user = request.user
    profile_obj = getattr(user, 'profile', None)
    posts = BlogPost.objects.filter(author=user).order_by('-pub_date')

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile_obj)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=profile_obj)

    return render(request, 'profile.html', {
        'user': user,
        'profile': profile_obj,
        'profile_form': profile_form,
        'posts': posts
    })
    
    

