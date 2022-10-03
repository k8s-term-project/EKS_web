from django.contrib.auth.decorators import login_required
from django.core.mail.backends import console
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cluster
from .form import ClusterForm
import os, subprocess

def index(request):
    project_list = Cluster.objects.order_by('-project_name')
    context = {'project_list':project_list}
    return render(request, 'EKS/index.html', context)
# Create your views here.

def detail(request, project_name):
    project = Cluster.objects.get(project_name=project_name)
    context = {'project_name':project}
    return render(request, 'EKS/project_detail.html', context)

@login_required(login_url = '/user/login')
def createCluster(request):
    if request.method == "GET":
        clusterForm = ClusterForm()
        context = {'clusterForm': clusterForm}
        return render(request, "EKS/forms.html", context)
    elif request.method == "POST":
        clusterForm = ClusterForm(request.POST)
        if clusterForm.is_valid():
            cluster = clusterForm.save(commit=False)
            cluster.email = request.user
            cluster.save()
            data = " "
            data += str(cluster.email)
            data += " "
            data += str(cluster.nodes)
            data += " "
            data += str(cluster.vcpu)
            data += " "
            data += str(cluster.ram)
            excute = "/root/data.sh"
            excute += data
            print(excute)
            subprocess.run([excute], shell=True)

        return redirect('/')

@login_required(login_url = '/user/login')
def deleteCluster(request, project_name):
    cluster = Cluster.objects.get(project_name=project_name)
    if request.user != cluster.email:
        return redirect('/')
    else:
        cluster.delete()
        return redirect('/')

