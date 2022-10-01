from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cluster
from .form import ClusterForm
def index(request):
    project_list = Cluster.objects.order_by('-project_name')
    context = {'project_list':project_list}
    return render(request, 'EKS/index.html', context)
# Create your views here.

def detail(request, project_name):
    project = Cluster.objects.get(project_name=project_name)
    context = {'project_name':project}
    return render(request, 'EKS/project_detail.html', context)

def createCluster(request):
    if request.method == "GET":
        clusterForm = ClusterForm()
        context = {'clusterForm': clusterForm}
        return render(request, "EKS/forms.html", context)
    elif request.method == "POST":
        clusterForm = ClusterForm(request.POST)
        if clusterForm.is_valid():
            cluster = clusterForm.save(commit=False)
            cluster.save()
        return redirect('/')

def deleteCluster(request, project_name):
    cluster = Cluster.objects.get(project_name=project_name)
    cluster.delete()
    return redirect('/')