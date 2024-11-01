from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0,'Draft'),(1,'Published'))

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    # link(Friendly Url for navigation)
    slug = models.SlugField(max_length=100, unique=True)
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering=['created_at']

    def __str__(self):
        return self.title

#assuming you are creating a blog app and maybe you have unfinished posts that you dont want published yet


