from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    Status_Choices=(('draft','Draft'),('published','Published'))
    title =models.CharField(max_length=256)
    slug=models.SlugField(max_length=256,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body=models.CharField(max_length=1000)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=50,choices=Status_Choices,default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),
        self.publish.strftime('%d'),self.slug])

class Comments(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comm')
    name=models.CharField(max_length=50)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return 'Commented by{} on {}'.format(self.name,self.post)

class Login(models.Model):
    Username=models.EmailField()
    CreatePassword=models.CharField(max_length=50)
    RetypePassword=models.CharField(max_length=50)
