from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from main.models import Manufacturer, Cereal

from main.forms import ContactForm
from main.forms import CerealEditForm, CerealCreateForm
from main.forms import UserSignUp, UserLogin


def manuf_list(request):

    context = {}

    manufs = Manufacturer.objects.all()

    context['manufs'] = manufs

    cereal_v = request.POST.get('cereal_f', None)

    try:
        cereal_test = Cereal.objects.get(name=cereal_v)
        context['display_cereal'] = 0
    except Exception, e:
        if cereal_v == "" or cereal_v is None:
            context['display_cereal'] = 1
        else:
            context['display_cereal'] = 2
            context['not_in_db'] = cereal_v

    if cereal_v is not None:
        cereals = Cereal.objects.filter(name__icontains=cereal_v)
        for cereal in cereals:
            cereal = cereal.replace("_", " ")
    else:
        cereals = [cereal_v]

    context['cereals'] = cereals

    return render_to_response('manuf_list.html', context,
                              context_instance=RequestContext(request))


def cer_by_manuf_list(request, pk):
    context = {}

    manufs = Manufacturer.objects.all()

    context['manufs'] = manufs

    return render_to_response('cer_by_manuf_list.html', context,
                              context_instance=RequestContext(request))


def manuf_detail(request, pk):
    context = {}

    manuf = Manufacturer.objects.get(pk=pk)

    context['manuf'] = manuf

    return render_to_response('manuf_detail.html', context,
                              context_instance=RequestContext(request))


def cereal_detail(request, pk):
    context = {}

    cereal = Cereal.objects.get(pk=pk)

    context['cereal'] = cereal

    return render_to_response('cereal_detail.html', context,
                              context_instance=RequestContext(request))


def cereal_create(request):

    context = {}

    context['manufs'] = Manufacturer.objects.all

    form_cereal_create = CerealCreateForm()
    context['form_cereal_create_v'] = form_cereal_create

    if request.method == 'POST':
        form_cereal_create2 = CerealCreateForm(request.POST)
        if form_cereal_create2.is_valid():
            form_cereal_create2.save()
            return HttpResponseRedirect('/manuf_list')
        else:
            context['errors'] = form_cereal_create2.errors

    return render_to_response('cereal_create.html', context,
                              context_instance=RequestContext(request))
