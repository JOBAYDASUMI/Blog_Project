from django.db import models

from django.contrib.auth.models import AbstractUser


class Custom_user(AbstractUser):
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    
    USER=[
        ('viewers','Viewers'),
        ('bloogger','Bloogger'),
    ]
    
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    Gender=models.CharField(choices=GENDER, max_length=100,null=True)
    Age=models.PositiveIntegerField(null=True)
    Contact_No=models.CharField(max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to="Media/Profile_Pic",null=True)
    
    def __str__(self):  
        
        return f"{self.username}-{self.Age}"
    
    
class viewersProfileModel(models.Model):
    
    PREFERRED_CONTENT=[
        ('articles','Articles'),
        ('videos','Videos'),
        ('both','Both'),
    ]
    
    user=models.OneToOneField(Custom_user,on_delete=models.CASCADE,related_name='viewersProfile')
    Bio=models.CharField(max_length=100,null=True)
    interest=models.CharField(max_length=100,null=True)
    preferred_content_type=models.CharField(max_length=100,null=True,choices=PREFERRED_CONTENT,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.user.username}"   
    
    
class BloggerProfileModel(models.Model):
    
    
    
    user=models.OneToOneField(Custom_user,on_delete=models.CASCADE,related_name='bloggerProfile')
    Bio=models.CharField(max_length=100,null=True)
    website_url=models.URLField(blank=True,null=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.user.username}"    
    
class BlogPostModel(models.Model):
    
    CATEGORY=[
        ('Technology','Technology'),
        ('Sports','Sports'),
        ('Entertainment','Entertainment'),
        ('Politics','Politics'),
        ('Business','Business'),
        ('Health','Health'),
        ('Education','Education'),
        ('Travel','Travel'),
        ('Food','Food'),
        ('Fashion','Fashion'),
    ]
    
    user=models.ForeignKey(Custom_user,on_delete=models.CASCADE)
    
    BlogTitle=models.CharField(max_length=500,null=True)
    BlogBody=models.TextField(null=True)
    Category=models.CharField(choices=CATEGORY, max_length=100,null=True)
    Blog_Pic=models.ImageField(upload_to='Media/Blog_Pic',null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)
    
    
    def __str__(self):
        return f"Username: {self.user.username} - Blog Title : {self.BlogTitle} " 
