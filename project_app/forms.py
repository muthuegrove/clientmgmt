from django.forms import ModelForm
from models import Project

class ProjectCreationForm(ModelForm):
    '''
    Project creation form
    '''
    class Meta:
        model = Project
        fields = '__all__'