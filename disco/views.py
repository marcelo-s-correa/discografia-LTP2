from django.shortcuts import render , redirect
from .models import Musica
from .forms import FormMusicas

def musica_list(request):
    musicas = Musica.objects.all()
    template_name = 'musica_list.html'
    context = {
        'musica_list': musicas,
    }
    return render(request, template_name, context)

def musica_new(request):
    if request.method == "POST":
        form = FormMusicas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disco:musica_list')
    else:
        form = FormMusicas()
    template_name = 'musica_new.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)

def musica_delete(request,pk):
    musica = Musica.objects.get(pk=pk)
    musica.delete()
    return redirect('disco:musica_list')

def musica_edit(request,pk):
    musica = Musica.objects.get(pk=pk)
    if request.method == 'POST':
        form = FormMusicas(request.POST,instance=musica)
        if form.is_valid():
            form.save()
            return redirect('disco:musica_list')
    else:
        form = FormMusicas(instance=musica)
    template_name = 'musica_edit.html'
    context = {
        'form': form,
        'pk': pk
    }
    return render(request, template_name, context)

def relatorio(request):
    musicas = Musica.objects.all()
    template_name = 'relatorio.html'
    lst_musica = []
    lst_seg = []
    for m in musicas:
        lst_musica.append(m.titulo)
        lst_seg.append(m.segundos)
    
    print(lst_musica,lst_seg)
    context = {
        'relatorio': musicas,
        'lst_musica': lst_musica,
        'lst_seg': lst_seg,

    }
    return render(request, template_name, context)
