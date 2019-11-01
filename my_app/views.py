from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Blog, Comment, User
from .forms import UserForm


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        # 继承View类,重写get函数
        blog_obj = Blog.objects.all()
        return render(request, 'index.html', {'blog_obj': blog_obj})


class BlogsView(View):
    def get(self, request, *args, **kwargs):
        blog_obj = Blog.objects.all()
        return render(request, 'blog.html', {'blog_obj': blog_obj})


class PostView(View):
    def get(self, request, b_id, *args, **kwargs):
        blog = Blog.objects.filter(id=b_id).first()
        blogobj = Blog.objects.all()
        comments = Comment.objects.filter(blog=b_id).all()
        obj_dict = {
            'blog': blog,
            'blog_obj': blogobj,
            'comments': comments
        }
        return render(request, 'post.html', obj_dict)

    def post(self, request, b_id, *args, **kwargs):
        form = UserForm(request.POST)
        blog_obj = Blog.objects.filter(id=b_id).first()
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            comment = form.cleaned_data.get('comment')
            print(username,email,comment)
            user = User.objects.filter(user_name=username, user_email=email).first()
            if user:
                Comment.objects.create(comment_content=comment, user=user, blog=blog_obj)
            else:
                User.objects.create(user_name=username, user_email=email)
                user = User.objects.filter(user_name=username, user_email=email).first()
                Comment.objects.create(comment_content=comment, user=user, blog=blog_obj)
            blog_obj.comment_count += 1
            blog_obj.save()

        # username = request.POST.get("username")
        # email = request.POST.get("email")
        # comment = request.POST.get("comment")
        # user = User.objects.filter(user_name=username, user_email=email).first()
        # uf = UserForm(request.POST)

        #
        # # print(user.u_id)
        #
        # if uf.is_valid():
        #     if user:
        #         print('enter...have user')
        #         Comment.objects.create(comment_content=comment, user=user, blog=blog_obj)
        #     else:
        #         print('enter...no user')
        #         User.objects.create(user_name=username, user_email=email)
        #         user = User.objects.filter(user_name=username, user_email=email).first()
        #         Comment.objects.create(comment_content=comment, user=user, blog=blog_obj)
        return redirect('/post/%s' %(b_id))