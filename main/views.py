from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from main.models import Manufacturer, Cereal
from django.template import RequestContext


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

    context['request'] = request.method

    context['manufs'] = Manufacturer.objects.all

    if request.method == 'POST':
        name_v = request.POST.get('name_f', None)
        manuf_name_v = request.POST.get('manuf_name_f', None)
        cer_type_v = request.POST.get('cer_type_f', None)
        calories_v = request.POST.get('calories_f', None)
        protein_v = request.POST.get('protein_f', None)
        fat_v = request.POST.get('fat_f', None)
        sodium_v = request.POST.get('sodium_f', None)
        fiber_v = request.POST.get('fiber_f', None)
        carbs_v = request.POST.get('carbs_f', None)
        sugars_v = request.POST.get('sugars_f', None)
        potassium_v = request.POST.get('potassium_f', None)
        vits_mins_v = request.POST.get('vits_mins_f', None)
        ss_weight_v = request.POST.get('ss_weight_f', None)
        cups_per_s_v = request.POST.get('cups_per_s_f', None)
        manuf_id_v = request.POST.get('manuf_id', None)

        if manuf_id_v is not None:
            manuf = Manufacturer.objects.get(pk=manuf_id_v)
        else:
            manuf = Manufacturer.objects.get(name='Nabisco')

        # in the get_or_create(name=name_v), "name" has to match the column
        # header in the source database
        the_cereal, created = Cereal.objects.get_or_create(name=name_v)

        # in the sequence below, the attributes of the_cereal (eg,
        # the_cereal.manuf) has to match the column header in the db
        the_cereal.manuf = manuf
        the_cereal.cer_type = cer_type_v
        the_cereal.calories = calories_v
        the_cereal.protein = protein_v
        the_cereal.fat = fat_v
        the_cereal.sodium = sodium_v
        the_cereal.fiber = fiber_v
        the_cereal.carbs = carbs_v
        the_cereal.sugars = sugars_v
        the_cereal.potassium = potassium_v
        the_cereal.vits_mins = vits_mins_v
        the_cereal.ss_weight = ss_weight_v
        the_cereal.cups_per_s = cups_per_s_v

        the_cereal.save()

        context['created'] = 'Operation Successful'
    elif request.method == 'GET':
        print "It was a GET request."

    return render_to_response('cereal_create.html', context,
                              context_instance=RequestContext(request))
