from django.contrib.auth import authenticate, login
#from django.shortcuts import render
#from django.core.exceptions import DoesNotExist
#from django.contrib.auth.models import User
#from . models import Asset_Login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import logout



# Create your views here.
def home(request):
    return render(request,'home.html')
def prpty_mng(request):       
    return render(request,'prpty_mng.html')
def amc_mng(request):
    return render(request,'amc_mng.html')
def store_mng(request):
    return render(request,'store_mng.html')
def rem_schedule(request):
    return render(request,'rem_schedule.html')
def vehicle_mng(request):
    return render(request,'vehicle_mng.html')
def build_mnt(request):
    return render(request,'build_mnt.html')
def iso_mng(request):
    return render(request,'iso_mng.html')
def house_mng(request):
    return render(request,'house_mng.html')
def purchase_mng(request):
    return render(request,'purchase_mng.html')
def tax_building(request):
    return render(request,'tax_building.html')
def tenant_mng(request):
    return render(request,'tenant_mng.html')




def asset_login(request):
    if request.method == 'POST':
        username = request.POST['user_id']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username, password=password)
            if user:
                if user.position == 'admin':
                    return redirect('admin_dashboard')
                elif user.position == 'user':
                    return redirect('viewer_dashboard')
                else:
                    messages.error(request, 'Unknown user position')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'asset_mng.html')

def logout_view(request):
    logout(request)
    return redirect('asset_login')


def admin_dashboard(request):
    username =request.user.username
    return render(request, 'admin.html', {'username': username})




def viewer_dashboard(request):
    username = request.user.username
    return render(request, 'user.html', {'username': username})