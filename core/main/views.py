from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView , View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from .models import *
from .forms import *
# Create your views here.

class homeListView(ListView):
    template_name = 'index.html'

    def get(self , request):
        header_list = h_Header.objects.all()
        have_list = h_what_do_we_have.objects.all()
        About_list = About.objects.all()
        Classes_list = Classes.objects.all()
        Blog_list = Blog.objects.all()
        students_list = students.objects.all()
        footer_list = footer.objects.all()
        context = {
            'header_list':header_list,
            'have_list':have_list,
            'About_list':About_list,
            'Classes_list':Classes_list,
            'Blog_list':Blog_list,
            'students_list':students_list,
            'footer_list':footer_list
        }
        return render(request , self.template_name , context)










# user
def user_login(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, (f'You Have Been Logged In Successfully. Welcome! {username} '))
                return redirect('home')
            else:
                messages.success(request, ("Something went wrong username or password is wrong, Please try again!"))
                return redirect('login')
            
        else:
            return render(request, 'login.html', {})




def user_logout(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')



def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"You have registered successfully! Welcome, {username}!")
            return redirect('home')
        else:
            # Отображаем ошибки
            messages.error(request, "Oops! There was a problem registering, please try again.")
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})
    

