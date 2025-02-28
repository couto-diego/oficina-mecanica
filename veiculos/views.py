# veiculos/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Veiculo
from .forms import VeiculoForm

def veiculo_list(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculos/veiculo_list.html', {'veiculos': veiculos})

def veiculo_create(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veiculo_list')
    else:
        form = VeiculoForm()
    return render(request, 'veiculos/veiculo_form.html', {'form': form})

def veiculo_update(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('veiculo_list')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'veiculos/veiculo_form.html', {'form': form})

def veiculo_delete(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('veiculo_list')
    return render(request, 'veiculos/veiculo_confirm_delete.html', {'veiculo': veiculo})