from django.shortcuts import render
from django.http import HttpResponse
from .models import Cluster

def index(request):
    project_list = Cluster.objects.order_by('-create_date')
    context = {'project_list':project_list}
    return render(request, 'EKS/index.html', context)
# Create your views here.

def detail(request, project_name):
    project = Cluster.objects.get(project_name=project_name)
    context = {'project_name':project}
    return render(request, 'EKS/project_detail.html', context)