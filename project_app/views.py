import datetime

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
    current_week_project = []
    current_month_project = []
    current_year_project = []

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

    if project_list:
        new_project_list = get_week_month_year(project_list)
        current_week_project = new_project_list[0]
        current_month_project = new_project_list[1]
        current_year_project = new_project_list[2]

    return render(request, 'projects_management.html', {'project_list': project_list,
                                                        'current_week_project': current_week_project,
                                                        'current_month_project': current_month_project,
                                                        'current_year_project': current_year_project,
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


def get_week_month_year(project_list):
    today = datetime.date.today()
    start_week = today - datetime.timedelta(today.weekday())
    end_week = start_week + datetime.timedelta(7)
    current_week_project = project_list.filter(start_date__range=[start_week, end_week])
    current_year_project = project_list.filter(start_date__year=today.year)
    current_month_project = current_year_project.filter(start_date__month=today.month)

    return current_week_project, current_month_project, current_year_project
