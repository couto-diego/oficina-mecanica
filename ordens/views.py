# ordens/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import OrdemServico
from .forms import OrdemServicoForm

def ordem_servico_list(request):
    # Lista todas as ordens de serviço
    ordens = OrdemServico.objects.all()
    return render(request, 'ordens/ordem_servico_list.html', {'ordens': ordens})

def ordem_servico_create(request):
    # Cria uma nova ordem de serviço
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            ordem = form.save()  # Salva a ordem de serviço
            ordem.calcular_valor_total()  # Calcula o valor total
            return redirect('ordem_servico_list')  # Redireciona para a lista de ordens
    else:
        form = OrdemServicoForm()
    return render(request, 'ordens/ordem_servico_form.html', {'form': form})

def ordem_servico_update(request, pk):
    # Edita uma ordem de serviço existente
    ordem = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST, instance=ordem)
        if form.is_valid():
            ordem = form.save()  # Salva as alterações
            ordem.calcular_valor_total()  # Recalcula o valor total
            return redirect('ordem_servico_list')  # Redireciona para a lista de ordens
    else:
        form = OrdemServicoForm(instance=ordem)
    return render(request, 'ordens/ordem_servico_form.html', {'form': form})

def ordem_servico_delete(request, pk):
    # Exclui uma ordem de serviço
    ordem = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        ordem.delete()  # Remove a ordem de serviço
        return redirect('ordem_servico_list')  # Redireciona para a lista de ordens
    return render(request, 'ordens/ordem_servico_confirm_delete.html', {'ordem': ordem})