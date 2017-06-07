from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

# Create your views here.
from blog.models import Post, Comment


def home(request):
    template_name = 'blog/home.html'
    posts = Post.objects.all()
    for i in posts:
        i.content = i.content[0:100]
    context = {'object_list': posts}
    return render(request, template_name, context)

def post_detail(request, pk):
    template_name = 'blog/post.html'
    post = Post.objects.get(id=int(pk))
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments':comments}
    print(comments)
    return render(request, template_name, context)


def add_post(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES['img']
        is_published = request.POST['is_published']
        user = User.objects.get(username=request.user.username)
        new_post= Post(title=title, user=user, content=content,img=img,is_published=is_published )
        new_post.save()
        redirect('post', new_post.id)
    else:
        template_name = 'blog/add_post.html'
        context = {}
        return render(request, template_name , context)

def edit_post(request, pk):
    post = Post.objects.get(id=int(pk))
    if request.user.username !=post.user.username:
        raise PermissionDenied
    if request.user.method == "GET":
        template_name ='blog/post_edit.html'
        context ={'post':post}
        return render(request,template_name,context)
    else:
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.is_published=request.POST['is_published']
        post.img=request.FILES['img']
        post.save()
        return redirect('post',post.id)

def delete_post(request , id):
    if Post.objects.get(id=id)is not None:
        post = Post.objects.get(id=id)
        if post.user.username == request.user.username:
            post.delete()
            return redirect('home')
        raise PermissionDenied


def signup(request):
    template = 'registration/signup.html'
    context = {}


    if  request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(User.objects.check())


        if len(User.objects.filter(email=email)) != 0:
            context['errors'] ="email is already taken"
            return render(request,template,context)

        user = User.objects.filter(username=username)

        if len(user) != 0:
            context['errors'] = "username is alreay taken "
            return render(request,template,context)

        if password1 == password2:
            user = User(first_name=firstname, last_name=lastname, email=email, username=username)
            user.set_password(password1)
            user.save()
            return redirect('login')
    return render(request,template,context)






