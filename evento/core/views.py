from django.shortcuts import render
from evento.core.forms import CoreForm


def home(request):
    return render(request, 'index.html', {'form': CoreForm()})