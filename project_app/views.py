from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from forms import ProjectCreationForm
from models import Project

def project_mgmt(request):
    '''
    Project Management Page
    '''
    project_list = Project.objects.all()

    return render(request, 'projects_management.html', {'project_list': project_list})


def create_project(request):
    '''
    Create Project Form
    '''
    form = ProjectCreationForm()
    if request.method == 'POST':
        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('project_mgmt'))
    return render(request, 'create_project_form.html', {'form': form})
    
