# mecanicos/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Mecanico
from .forms import MecanicoForm

def mecanico_list(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'mecanicos/mecanico_list.html', {'mecanicos': mecanicos})

def mecanico_create(request):
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mecanico_list')
    else:
        form = MecanicoForm()
    return render(request, 'mecanicos/mecanico_form.html', {'form': form})

def mecanico_update(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        form = MecanicoForm(request.POST, instance=mecanico)
        if form.is_valid():
            form.save()
            return redirect('mecanico_list')
    else:
        form = MecanicoForm(instance=mecanico)
    return render(request, 'mecanicos/mecanico_form.html', {'form': form})

def mecanico_delete(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        mecanico.delete()
        return redirect('mecanico_list')
    return render(request, 'mecanicos/mecanico_confirm_delete.html', {'mecanico': mecanico})
