from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# vamos ir cargando uno por uno los models para ver donde se encuentrar mi error

STATUS_CHOICES = (
        ('1', "DRAFT"),
        ('2', "PUBLISHED"),
        ('3', "REMOVED"),
    )  
COLOR_CHOICES = (
    ('1', 'celeste'),
    ('2', 'beige'),
    ('3', 'salmon')
)

NAME_CHOICES = (
    ('1', 'nacional'),
    ('2', 'provincial'),
    ('3', 'municipal')
)

class Category (models.Model):
    name= models.CharField(choices= NAME_CHOICES, default = 'nacional', max_length=20)
    description = models.TextField()
    slug = models.SlugField(null=False, blank=False, unique=True)
    color = models.CharField(max_length=10, choices= COLOR_CHOICES, default= 'celeste')

    def __str__(self):
        return self.name

class PostCategory (models.Model):
    post = models.ForeignKey('Post', on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    def __str__(self):
        return self.post.title + " - " + self.category.name

class Post(models.Model):
    title = models.CharField(max_length= 50, null=False)
    content = models.TextField(max_length= 300, null=False)
    create_at = models.DateField(auto_created=True)
    update_at = models.DateField(auto_now_add= True)
    category = models.ManyToManyField(Category,through='PostCategory')
    status = models.CharField(choices=STATUS_CHOICES , default= 'DRAFT', max_length=10)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to="image", null = True, blank = True)

    def __str__(self):
        return self.title

class Comment (models.Model):
    author = models.CharField(max_length= 20, null = False)
    content = models.TextField(null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add= True)
    comment_post = models.ForeignKey(Post, on_delete= models.CASCADE)

    def __str__(self):
        return self.author

