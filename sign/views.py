from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from . models import Asset_login
from .models import AssetTable



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

def admin_dashboard(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request, 'asset_mng/admin.html', {'username': username})

def head_dashboard(request):
    username = request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/head.html',{'username' : username})

def ciso_dashboard(request):
    username = request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/ciso.html',{'username' : username})

def asset_owner_dashboard(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request, 'asset_mng/asset_owner.html', {'username': username})

def asset_login(request):
    if request.method == 'POST':
        username = request.POST['user_id']
        password = request.POST['password']

        try:
            user = Asset_login.objects.get(username=username, password=password)
            if user is not None:
                request.session['username'] = user.username
                if user.position == 'admin':
                    return redirect('admin_dashboard')
                elif user.position == 'head':
                    return redirect('head_dashboard')
                elif user.position == 'asset_owner':
                    return redirect('asset_owner_dashboard')
                elif user.position == 'ciso':
                    return redirect('ciso_dashboard')
                else:
                 messages.error(request, 'Unknown user position')
            else:
                messages.error(request, 'Invalid username or password')
        except Asset_login.DoesNotExist:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'asset_mng/asset_mng.html')


def privileges(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privileges.html',{'username':username})

def privilege_admin(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privilege_admin.html',{'username':username})

def privilege_ciso(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privilege_ciso.html',{'username':username})

def privilege_head(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privilege_head.html',{'username':username})

def privilege_asset_owner(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privilege_asset_owner.html',{'username':username})

def logout_view(request):
    logout(request)
    return redirect('asset_login')

def asset_list(request):
    users=AssetTable.objects.all()
    return render(request,'asset_mng/asset_pro.html',{'users':users})
