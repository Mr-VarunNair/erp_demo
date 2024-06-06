from django.shortcuts import render

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
def asset_mng(request):
    return render(request,'asset_mng.html')
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