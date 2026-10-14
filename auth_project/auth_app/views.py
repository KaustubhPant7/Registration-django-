from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from .forms import UserCreationForm

# Create your views here.
def dashboard(request):
  return render(request,'home.html')

def register_view(request):
  form = UserCreationForm()
  context ={'form':form}
  return render(request, 'registration/register.html',context)




# def register(request):
#   if request.method =="POST":
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       login(request, user)
#       return HttpResponse('Registration successful')
#     else:
#       form = UserCreationForm()
#   return render(request,'auth/register.html',{'form':form}) 



# def login_view(request):
#   pass



# def logout(request):
#   pass