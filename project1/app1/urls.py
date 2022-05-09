from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('ev/', views.employeeView, name='emp_url'),
    path('se/', views.showEmpView, name='showemp_url'),
    path('ue/<int:id>/', views.updateEmpView, name='updateEmp_url'),
    path('de/<int:id>/', views.deleteEmpView, name='deleteEmp_url')
]