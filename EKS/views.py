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
    context = {'project':project}
    return render(request, 'EKS/project_detail.html', context)

@login_required(login_url = '/user/login')
def createCluster(request):
    if request.method == "GET":
        clusterForm = ClusterForm()
        context = {'clusterForm': clusterForm}
        return render(request, "EKS/create.html", context)
        # return render(request, "EKS/forms.html", context)
    elif request.method == "POST":
        clusterForm = ClusterForm(request.POST)
        if clusterForm.is_valid():
            cluster = clusterForm.save(commit=False)
            cluster.email = request.user
            cluster.save()
            data = " "
            data += str(cluster.email)
            data += " "
            data += str(cluster.project_name)
            data += " "
            data += str(cluster.master_num)
            data += " "
            data += str(cluster.master_cpu)
            data += " "
            data += str(cluster.master_ram)
            data += " "
            data += str(cluster.master_disk)
            data += " "
            data += str(cluster.node_num)
            data += " "
            data += str(cluster.node_cpu)
            data += " "
            data += str(cluster.node_ram)
            data += " "
            data += str(cluster.node_disk)

            excute = "/root/create_instance.sh"
            excute += data
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
