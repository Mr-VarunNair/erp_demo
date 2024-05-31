from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'index.html')
def forgot_password(request):
    return render(request,'forgot_password.html')
def sign_up(request):
    return render(request,'sign_up.html')