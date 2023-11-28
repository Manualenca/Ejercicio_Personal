from django.contrib import admin
from .models import post, category, PostCategory, comment
# Register your models here.

admin.site.register(post)
admin.site.register(category)
admin.site.register(PostCategory)
admin.site.register(comment)

