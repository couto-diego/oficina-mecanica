
# pecas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Peca
from .forms import PecaForm

def peca_list(request):
    pecas = Peca.objects.all()
    return render(request, 'pecas/peca_list.html', {'pecas': pecas})

def peca_create(request):
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('peca_list')
    else:
        form = PecaForm()
    return render(request, 'pecas/peca_form.html', {'form': form})

def peca_update(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    if request.method == 'POST':
        form = PecaForm(request.POST, instance=peca)
        if form.is_valid():
            form.save()
            return redirect('peca_list')
    else:
        form = PecaForm(instance=peca)
    return render(request, 'pecas/peca_form.html', {'form': form})

def peca_delete(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    if request.method == 'POST':
        peca.delete()
        return redirect('peca_list')
    return render(request, 'pecas/peca_confirm_delete.html', {'peca': peca})