from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_category = models.DateTimeField(auto_now_add=True)
    updated_category = models.DateTimeField(auto_now=True)
     
    # Admin panel e Category er jaygay Categories Dekhanor jonno
    class Meta:
        verbose_name_plural ='Categories'