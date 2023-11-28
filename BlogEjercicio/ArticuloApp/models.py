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
    status = models.IntegerField(choices=STATUS_CHOICES , default= 1)
    slug = models.SlugField()
    image = models.ImageField(upload_to="image", null = True, blank = True)

    def __str__(self):
        return self.title
