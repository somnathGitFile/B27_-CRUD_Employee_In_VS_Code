from django.shortcuts import render, redirect
from.forms import EmployeeForm
from.models import Emplyee

# Create your views here.
def employeeView(request):
    form = EmployeeForm()
    template_name = 'app1/employee.html'
    context = {'form': form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showemp_url')
    return render(request, template_name, context)

def showEmpView(request):
    data = Emplyee.objects.all()
    template_name = 'app1/showEmp.html'
    context = {'obj': data}
    return render(request, template_name, context)

def updateEmpView(request, id):
    obj = Emplyee.objects.get(id=id)
    template_name = 'app1/employee.html'
    form = EmployeeForm(instance=obj)
    context = {'form': form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showemp_url')
    return render(request, template_name, context)


def deleteEmpView(request, id):
    obj = Emplyee.objects.get(id=id)
    template_name = 'app1/confirmation.html'
    context = {'obj': obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showemp_url')
    return render(request, template_name, context)

