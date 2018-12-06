from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django.urls import reverse
from django.apps import apps

# from .forms import IngestFileForm
# from .ingest import handle_file
from .models import Dataviz

import json

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Vizzes/index.html'
    context_object_name = 'latest_viz_list'
    def get_queryset(self):
        return Dataviz.objects.order_by('-date_added')[:5]
    
class VizView(generic.DetailView):
    model = Dataviz
    context_object_name = 'selected_dataviz'
    template_name = 'Vizzes/detail.html'

def pickModel(model):
    modelname = str(Dataviz.objects.get(model=model))
    return apps.get_model('vizzes', modelname, require_ready=True)

def VizData(request, **args):
    viz_id_arg = str(args['viz_id']).zfill(4)
    selected_model = pickModel(viz_id_arg)
    data = selected_model.objects.values()
    data = json.loads(json.dumps(data[0:len(data)]))
    return JsonResponse(data, safe=False)