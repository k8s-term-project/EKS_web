from django import forms
from EKS.models import Cluster

"""
class ClusterForm(forms.Form):
    email = forms.CharField()
    project_name = forms.CharField()
    description = forms.CharField()
    nodes = forms.IntegerField()
    vcpu = forms.IntegerField()
    ram = forms.IntegerField()
"""

class ClusterForm(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = ['project_name', 'description',
                  'master_num', 'master_cpu', 'master_ram',
                  'node_num', 'node_cpu', 'node_ram']
        exclude = ['email']