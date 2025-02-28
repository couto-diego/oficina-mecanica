# ordens/forms.py
from django import forms
from .models import OrdemServico

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        exclude = ['data_emissao']  # Exclui o campo 'data_emissao'
        widgets = {
            'data_conclusao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'descricao_defeito': forms.Textarea(attrs={'class': 'form-control'}),
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
            'mecanico': forms.Select(attrs={'class': 'form-control'}),
            'servicos': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'pecas': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pecas'].required = False  # Tornar o campo opcional
        self.fields['servicos'].required = False  # Tornar o campo opcional