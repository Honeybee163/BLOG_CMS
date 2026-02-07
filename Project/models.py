from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_images/', null=True, blank=True)


class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
   
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    
    

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=100)
    featured_image=models.ImageField(upload_to='images/',blank=True,null=True)
    status=models.CharField(max_length=10,choices=(('Draft','Draft'),('Published','Published')))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    
    






class Comment(models.Model):
    text=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text