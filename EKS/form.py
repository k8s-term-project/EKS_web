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
        fields = ['email', 'project_name', 'description',
                  'nodes', 'vcpu', 'ram']