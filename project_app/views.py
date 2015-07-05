from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from forms import ProjectCreationForm
from models import Project
from client_app.models import Client

def project_mgmt(request, **kwargs):
    '''
    Project Management Page
    '''
    client = None
    project_list = []

    try:
        client_id = int(kwargs['client_id'])
        client = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        messages.error(request, 'Client Not Available')
        return HttpResponseRedirect('/')
    except KeyError:
        client_id = None

    client_list = Client.objects.all()
    if client:
        project_list = Project.objects.filter(client=client)
    elif client_list:
        client = client_list[0]
        client_id = client.id
        project_list = Project.objects.filter(client=client)
    else:
        messages.error(request, "Client Not Available")
    
    return render(request, 'projects_management.html', {'project_list': project_list,
                                                        'client_list': client_list,
                                                        'client_id': client_id})


def create_project(request, **kwargs):
    '''
    Create Project Form
    '''
    form = ProjectCreationForm()
    project = None
    try:
        project_id = kwargs['project_id']
        project = Project.objects.get(id=project_id)
        form = ProjectCreationForm(instance=project)
    except:
        pass
    if request.method == 'POST':
        if project:
            form = ProjectCreationForm(request.POST, instance=project)
        else:
            form = ProjectCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('project_mgmt'))
    return render(request, 'create_project_form.html', {'form': form})
    
