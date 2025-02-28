# servicos/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Servico
from .forms import ServicoForm

def servico_list(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/servico_list.html', {'servicos': servicos})

def servico_create(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servico_list')
    else:
        form = ServicoForm()
    return render(request, 'servicos/servico_form.html', {'form': form})

def servico_update(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect('servico_list')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'servicos/servico_form.html', {'form': form})

def servico_delete(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        servico.delete()
        return redirect('servico_list')
    return render(request, 'servicos/servico_confirm_delete.html', {'servico': servico})