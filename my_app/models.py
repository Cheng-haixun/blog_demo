from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=16,verbose_name='用户名')
    user_email = models.TextField(verbose_name='用户邮箱')

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name

class Blog(models.Model):
    blog_title = models.CharField(max_length=32,verbose_name='博文标题')
    blog_detail = models.TextField(verbose_name='博文详情')
    create_date = models.DateTimeField(auto_now=True,verbose_name='创建时间')
    blog_photo = models.TextField(verbose_name='博文图片')
    comment_count = models.IntegerField(default=0,verbose_name='评论数')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='User外键')

    class Meta:
        verbose_name = '博客详情表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    comment_content = models.TextField(verbose_name='评论内容')
    comment_date = models.DateTimeField(auto_now=True,verbose_name='评论时间')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='User外键')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,verbose_name='Blog外键')

    class Meta:
        verbose_name = '评论表'
        verbose_name_plural = verbose_name