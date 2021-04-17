from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from univesp.models import AlunoUnivesp
from django.views import generic

from django import forms
# Create your views here.

class PostForm(forms.ModelForm):
    class Meta:
        model = AlunoUnivesp
        fields = ['nome', 'sobrenome', 'matricula',]


def index(request):
    alunos = AlunoUnivesp.atributos.all()
    contexto = {'alunos': alunos}
    return render(request, 'univesp/index.html', contexto)

def alterar(request, id):
    aluno = AlunoUnivesp.atributos.get(id = id)
    form = PostForm(request.POST or None, instance=aluno) #já vai começar preenchido

    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, 'univesp/cadastrar.html', {'form': form, 'aluno': aluno})

def cadastrar(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'univesp/cadastrar.html', {'form': form})

def delete(request, id):
    aluno = AlunoUnivesp.atributos.get(id = id)
    aluno.delete()
    return redirect('index')

