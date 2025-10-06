from django.shortcuts import render, redirect, get_object_or_404

from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    pendentes = Item.objects.filter(comprado=False) # Filtra os itens que não foram comprados
    carrinho = Item.objects.filter(comprado=True) # Filtra os itens que foram

    return render(request, 'index.html', 
        {'pendentes': pendentes,
        'carrinho': carrinho}) # Passa os itens para o template

def adicionar_item(request):
    if request.method == 'POST':
        formulario = ItemForm(request.POST) # Recebe os dados do formulário
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = ItemForm()
    return render(request, 'adicionar_item.html', {'formulario': formulario}) # Passa o formulário para o template

def editar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id) # Obtém o item ou retorna 404 se não encontrado
    if request.method == 'POST':
        formulario = ItemForm(request.POST, instance=item) # Preenche o formulário com os dados do item existente
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = ItemForm(instance=item)
    return render(request, 'editar_item.html', {'formulario': formulario}) # Passa o formulário para o template

def excluir_item(request, item_id):
    item = get_object_or_404(Item, id=item_id) # Obtém o item ou retorna 404 se não encontrado
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'excluir_item.html', {'item': item}) # Passa o item para o template

def adicionar_carrinho(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.comprado = True
    item.save()
    return redirect('index')

def remover_carrinho(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.comprado = False
    item.save()
    return redirect('index')