
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginPage,name='loginPage'),
    path('homePage/',homePage,name='homePage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('registerPage/',registerPage,name='registerPage'),
    path('profilePage/',profilePage,name='profilePage'),
    
    path('addJob/',addJob,name='addJob'),
    path('createdJob/',createdJob,name='createdJob'),
    
    path("editBlog/<str:id>", editBlog, name="editBlog"),
    path("deleteBlog/<str:id>", deleteBlog, name="deleteBlog"),
    
    path("AllBlogPost/", AllBlogPost, name="AllBlogPost"),
    path("viewSingleBlog/<str:id>", viewSingleBlog, name="viewSingleBlog"),
    path("search_blog/", search_blog, name="search_blog"),
    
    path('editProfilePage/',editProfilePage, name='editProfilePage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
