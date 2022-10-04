from django import forms
from EKS.models import Cluster

class ClusterForm(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = ['project_name', 'description',
                  'master_num', 'master_cpu', 'master_ram', 'master_disk',
                  'node_num', 'node_cpu', 'node_ram', 'node_disk']
        exclude = ['email']