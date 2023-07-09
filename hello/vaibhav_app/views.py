from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from vaibhav_app.models import Contact,Blog_Post,Cposting,Post,BlogComment
from django.contrib.auth  import authenticate,login, logout


# Create your views here.






def index(request):
    
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
    #return HttpResponse("this is vaibhav_app_about page")

def post(request):
    return render(request,"post.html")
def blog(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request,"blog.html",context)
def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post)
    context={'post':post, 'comments': comments}
    return render(request, "blogPost.html", context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        print("hello",name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,"contacts.html")



def search(request):
    query=request.GET['query']
    if(len(query)>20): # Removed query of big length greater than 20 characters 
        allPosts=[]
    elif(len(query)==0):
        messages.warning(request, 'Query was empty!')
        allPosts=[]
    else:
        allPosts= Post.objects.filter(title__icontains=query)
    
    params={'allPosts': allPosts,'query':query}
    return render(request,"search.html", params)

def handleSignup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if(pass1!=pass2):
            messages.warning(request, " passwords do not match ")
            return redirect('vaibhav_app')
        
        # Create the user           USER COMES FROM "from django.contrib.auth.models import User "
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('vaibhav_app')

    else:
        return HttpResponse("404 - Not found")
        
def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user=authenticate(username= loginusername, password= loginpass)            # authenticate,login,logout COMES FROM "from django.contrib.auth  import authenticate,login, logout"
        if (user):
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("vaibhav_app")
        else:
            messages.warning(request, "Invalid credentials! Please try again")
            return redirect("vaibhav_app")
    return HttpResponse("this is vaibhav_app_handleLogin page")  
    
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("vaibhav_app")

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=BlogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")