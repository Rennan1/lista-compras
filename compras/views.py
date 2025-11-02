from django.shortcuts import render, redirect, get_object_or_404

from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    ordem = request.GET.get('ordem', 'nome')  # padrão = ordem alfabética

    if ordem == 'nome':
        pendentes = Item.objects.filter(comprado=False).order_by('nome')
        carrinho = Item.objects.filter(comprado=True).order_by('nome')
    elif ordem == '-nome':
        pendentes = Item.objects.filter(comprado=False).order_by('-nome')
        carrinho = Item.objects.filter(comprado=True).order_by('-nome')
    elif ordem == 'recentes':
        pendentes = Item.objects.filter(comprado=False).order_by('-id')
        carrinho = Item.objects.filter(comprado=True).order_by('-id')
    elif ordem == 'antigos':
        pendentes = Item.objects.filter(comprado=False).order_by('id')
        carrinho = Item.objects.filter(comprado=True).order_by('id')
    else:
        pendentes = Item.objects.filter(comprado=False)
        carrinho = Item.objects.filter(comprado=True)


    return render(request, 'index.html', 
        {'pendentes': pendentes,
        'carrinho': carrinho,
        'ordem': ordem}) # Passa os itens para o template

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

def limpar_carrinho(request):
    Item.objects.filter(comprado=True).update(comprado=False) # Marca todos os itens como não comprados
    return redirect('index')