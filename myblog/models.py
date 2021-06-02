from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    header_image=models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_DEFAULT,
                                 default=1)
    snippet = models.CharField(max_length=255, default="Click Link Above To Read Blog......")
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("home")

class Profile(models.Model):
    user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio= models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    instgram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    pintrest_url = models.CharField(max_length=255, null=True, blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments" ,on_delete=CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)













