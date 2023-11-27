from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
 
class CustomCategory(AbstractUser):
    NACIONAL = 'nacional'
    PROVINCIAL = 'provincial'
    MUNICIPAL = 'municipal'

    ROLE_CHOICES = [
        (NACIONAL = 'nacional'),
        (PROVINCIAL = 'provincial'),
        (MUNICIPAL = 'municipal'),
    ]

class CustomColor(AbstractUser):
    CELESTE = 'celeste'
    NARANJA = 'naranja'
    BEIGE = 'beige'

    ROLE_CHOICES = [ 
        (CELESTE = 'celeste'),
        (NARANJA = 'naranja'),
        (BEIGE = 'beige'),
    ] 

class Post(models.Model):
    title = models.CharField(max_length=20, null = False, on_delete=models.CASCADE)
    content = models.TextField(max_length=100, null = False)
    created_at = models.DateField(verbose_name="Fecha de creación", auto_now= True)
    update_at = models.DateField(verbose_name="Fecha de modificación", auto_now_add= True)
    category = models.ForeignKey(PostCategory, on_delete= models.CASCADE)
    status = models.CharField()
    slug = models.SlugField(max_length= 30, null=False)
    image = models.ImageField(upload_to="imagen", null=True, blank=True)
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.title
    

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    class Meta:
        verbose_name ='postcategory'
        verbose_name_plural ='postcategorys'
    
    def __str__(self):
        return self.post
    
class Category(models.Model):
    name = models.OneToOneField(CustomCategory, on_delete= models.CASCADE)
    description = models.TextField(max_length=40)
    slug = models.SlugField(max_length= 20, null = False)
    color = models.CharField(CustomColor)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categorys'
    
    def __str__(self):
        return self.name
