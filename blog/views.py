from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    posts=Post.objects.all() 
    # des=posts.desc[:5]
    context={'posts':posts}
    return render(request,'blog/index.html',context)
    
def bposts(request,id):
    pi=Post.objects.get(pk=id)
    context={'post':pi}
    return render(request,'blog/bposts.html',context)
    
def addpost(request):
    if request.method=='POST':
        fm=PostForm(request.POST)
        if fm.is_valid():
            title=fm.cleaned_data['title']
            desc=fm.cleaned_data['desc']
            pst=Post(title=title,desc=desc)
            pst.save()
            fm=PostForm()
    else:
        fm=PostForm()
    return render(request,'blog/addpost.html',{'form':fm})
    
def editpost(request,id):
    if request.method=='POST':
            pi=Post.objects.get(pk=id)  
            fm=PostForm(request.POST,instance=pi)
            if fm.is_valid():   
                fm.save()
    else:
        pi=Post.objects.get(pk=id)
        fm=PostForm(instance=pi)
        context={'form':fm}
    return render(request,'blog/editpost.html',context)
    
def deletepost(request,id):
    # if request.method=='POST':
    pi=Post.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')