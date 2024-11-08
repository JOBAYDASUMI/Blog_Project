from django.shortcuts import render,redirect,get_object_or_404
from myApp.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def homePage(request):
    
    return render(request,'homePage.html')

def logoutPage(request):
    
    logout(request)
    
    return redirect("loginPage")

def loginPage(request):
    if request.method == 'POST':
        Username=request.POST.get('username')
        Password=request.POST.get('password')
        try:
            user = authenticate(request,username=Username,password=Password)
            
            if user is not None:
                login(request,user)
                return redirect("homePage")
            else:
                return redirect("loginPage")
        except Custom_user.DoesNotExist:
            return redirect("loginPage")
            
                
    
    return render(request,'loginPage.html')

def registerPage(request):
    if request.method == 'POST':
        Username=request.POST.get('username')
        Email=request.POST.get('email')
        Password=request.POST.get('password')
        Confirm_password=request.POST.get('confirm_password')
        User_type=request.POST.get('user_type')
        Gender=request.POST.get('gender')
        Age=request.POST.get('age')
        Contact_no=request.POST.get('contact_no')
        Profile_pic=request.POST.get('profile_pic')
        if Password==Confirm_password:
            user=Custom_user.objects.create_user(
                username=Username,
                email=Email,password=Password,
                user_type=User_type,
                Gender=Gender,
                Age=Age,
                Contact_No=Contact_no,
                Profile_Pic=Profile_pic, 
            )
            if User_type == 'viewers':
                viewersProfileModel.objects.create(user=user)
                
            elif User_type == 'bloogger':
                BloggerProfileModel.objects.create(user=user)
                
                
            return redirect("loginPage")
        
        
    
    return render (request, 'registerPage.html')


def profilePage(request):
    
    return render(request, 'profilePage.html')

def addJob(request):
    
    current_user=request.user
    
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        category = request.POST['category']
        image = request.FILES['image']
        
        blog=BlogPostModel(
            user=current_user,
            BlogTitle=title,
            BlogBody=body,
            Category=category,
            Blog_Pic=image
        )
        
        blog.save()
        
        return redirect("createdJob")
    
    return render(request, 'addJob.html')


def editBlog(request,id):

    blog=BlogPostModel.objects.get(id=id)
    
    context={
            'blog':blog
        }
    
    current_user=request.user
    
    if request.method == 'POST':
        Id = request.POST['id']
        title = request.POST['title']
        body = request.POST['body']
        category = request.POST['category']
        image = request.FILES['image']
        
        blog=BlogPostModel(
            id=Id,
            user=current_user,
            BlogTitle=title,
            BlogBody=body,
            Category=category,
            Blog_Pic=image
        )
        
        blog.save()
        return redirect("createdJob")
    
    return render(request, 'editBlog.html',context)

def deleteBlog(request,id):
    
    blog=BlogPostModel.objects.get(id=id).delete()
    
    return redirect("createdJob")
    
    

def createdJob(request):
    
    current_user=request.user
    
    blog=BlogPostModel.objects.filter(user=current_user)
    
    context={
        'blog':blog
    }
    
    
    return render(request, 'createdJob.html',context)



def AllBlogPost(request):
    
    blog=BlogPostModel.objects.all()
    
    context={
        'blog':blog
    }
    
    return render(request,"AllBlogPost.html",context)

def viewSingleBlog(request,id):
    
    blog=BlogPostModel.objects.get(id=id)
    
    context={
        'blog':blog
    }
    return render(request,"viewSingleBlog.html",context)

def search_blog(request):
    
    query = request.GET.get('query')
    
    if query:
         blog = BlogPostModel.objects.filter(Q(BlogTitle__icontains=query) 
                                       |Q(Category__icontains=query) 
                                       |Q(BlogBody__icontains=query) 
                                       |Q(user__username__icontains=query)
                                       ) 
                                  
    else:
        blog = BlogPostModel.objects.none() 
    context={
        'blogs':blog,
        'query':query
    }
    return render(request,"search_blog.html",context)


def editProfilePage(request):
    
    current_user=request.user
    
    if request.method=='POST':
        #basic_information
        
        current_user.username=request.POST.get("username")
        current_user.first_name=request.POST.get("first_name")
        current_user.last_name=request.POST.get("last_name")
        current_user.email=request.POST.get("email")
        current_user.gender=request.POST.get("gender")
        current_user.age=request.POST.get("age")
        current_user.contact_no=request.POST.get("contact_no")
        current_user.profile_pic=request.FILES.get("profile_pic")
        current_user.save()
        
        
        
        if current_user.user_type=='viewers':
            # Get or create the seeker profile
            viewers_profile, created = viewersProfileModel.objects.get_or_create(user=current_user)

            viewers_profile.Bio = request.FILES.get("bio", viewers_profile.Bio)
            viewers_profile.interest = request.POST.get("interests", viewers_profile.interest)
            viewers_profile.preferred_content_type = request.POST.get("preferred_content_type", viewers_profile.preferred_content_type)
            viewers_profile.location = request.POST.get("location", viewers_profile.location)  
            viewers_profile.save() 
        elif current_user.user_type=='bloogger':
            bloogger, created = BloggerProfileModel.objects.get_or_create(user=current_user)

            bloogger.Bio = request.FILES.get("bio", bloogger.Bio)
            bloogger.website_url = request.POST.get("website_url", bloogger.website_url)
            bloogger.location = request.POST.get("location", bloogger.location)  
            bloogger.save()
        
        
        current_user.save() 
        
        return redirect("profilePage")
        
        
    
    return render(request,"editProfilePage.html")