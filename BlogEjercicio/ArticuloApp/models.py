from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# vamos ir cargando uno por uno los models para ver donde se encuentrar mi error

STATUS_CHOICES = (
        (1, "DRAFT"),
        (2, "PUBLISHED"),
        (3, "REMOVED"),
    )  

class post(models.Model):
    title = models.CharField(max_length= 20, null=False)
    content = models.TextField(max_length= 100, null=False)
    create_at = models.DateField(auto_created=True)
    update_at = models.DateField(auto_now_add= True)
    category = models.ManyToManyField("PostCategory")
    status = models.IntegerField(choices=STATUS_CHOICES , default= 1)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to="image", null = True, blank = True)

    def __str__(self):
        return self.title

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

class category (models.Model):
    name= models.TextField(choices= NAME_CHOICES, default = 'nacional')
    description = models.TextField()
    slug = models.SlugField(null=False, blank=False, unique=True)
    color = models.CharField(max_length=10, choices= COLOR_CHOICES, default= 'celeste')

    def __str__(self):
        return self.name

class PostCategory (models.Model):
    posts = models.ForeignKey(post, on_delete= models.CASCADE)
    categories = models.ForeignKey(category, on_delete= models.CASCADE)

    def __str__(self):
        return self.post

class comment (models.Model):
    author = models.CharField(max_length= 20, null = False)
    content = models.TextField(null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.author

