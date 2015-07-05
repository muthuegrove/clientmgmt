from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages

from models import Client
from forms import ClientCreationForm


def create_client(request):
    '''
    Client Management Page
    '''
    form = ClientCreationForm()
    if request.method == 'POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            company_info = form.cleaned_data['company_info']
            user = User.objects.create_user(username=username, email=email, password=username)
            user.is_active = True
            user.save()
            client = Client.objects.create(user=user, company_info=company_info)
            messages.success(request, 'Client Created successfully.')
            return HttpResponseRedirect(reverse('create_project'))

    return render(request, 'clients_create_form.html',{'form': form})