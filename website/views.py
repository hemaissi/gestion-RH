from django.shortcuts import render,redirect
from grh.models import Commune, Employee, Service, Travailler
from .forms import EmployeeForm

def index(request):
    return render(request,'index.html',{})

def home(request):
    all_Communes = Commune.objects.all()
    all_Employees = Employee.objects.all()
    all_Services = Service.objects.all()
    return render(request, 'home.html', {'allC': all_Communes,'allE':all_Employees,'allS':all_Services})
# Create your views here.

def join(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigez vers une page de succès

    else:
        form = EmployeeForm()

    all_Communes = Commune.objects.all()
    return render(request, 'join.html', {'allC': all_Communes, 'form': form})