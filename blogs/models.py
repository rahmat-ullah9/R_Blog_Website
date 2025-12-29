from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_category = models.DateTimeField(auto_now_add=True)
    updated_category = models.DateTimeField(auto_now=True)
     
    # Admin panel e Category er jaygay Categories Dekhanor jonno
    class Meta:
        verbose_name_plural ='Categories'


STATUS_CHOICE = (

    ('draft','Draft'),
    ('public','published')

)
class Blogs(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=1000)
    blog_body = models.TextField(max_length=3000)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    is_featured = models.BooleanField(default=False)
    
    created_category = models.DateTimeField(auto_now_add=True)
    updated_category = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural ='blogs'
