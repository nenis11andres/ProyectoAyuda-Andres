from django.shortcuts import render, redirect, get_object_or_404
from .models import Test, Pregunta, Respuesta
from usuarios_app.models import Usuario
from .forms import TestForm, PreguntaForm, RespuestaForm
from django.contrib import messages


# Create your views here.
def index(request):
    tests = Test.objects.all()

    return render(request, 'index_tests.html', { 'tests': tests })


def crear_test(request):
    test = Test()
    form = TestForm()

    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.autor = request.user
            test.save()
            messages.success(request, 'El test ha sido creado correctamente.')
            return redirect('index_tests')

    return render(request, 'crear_test.html', { 'form': form })


def ver_preguntas(request, pk):
    test = get_object_or_404(Test, pk=pk)
    preguntas = test.preguntas.all()

    return render(request, 'ver_preguntas.html', { 'preguntas': preguntas, 'test': test })


def agregar_pregunta(request, pk):
    test = get_object_or_404(Test, pk=pk)
    form = PreguntaForm()
    
    if request.method == "POST":
        form = PreguntaForm(request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.test = test
            pregunta.save()
            messages.success(request, 'La pregunta ha sido agregada correctamente.')
            return redirect('index_tests')

    return render(request, 'agregar_pregunta.html', { 'form': form })


def eliminar_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    test.delete()
    messages.warning(request, 'El test ha sido eliminado correctamente.')
    
    return redirect('index_tests')


def editar_pregunta(request, pkPregunta, pkTest):
    test = get_object_or_404(Test, pk=pkTest)
    pregunta = get_object_or_404(Pregunta, pk=pkPregunta)
    form = PreguntaForm()

    if request.method == "POST":
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            pregunta.save()
            messages.info(request, 'La pregunta ha sido editada correctamente.')
            return redirect('ver_preguntas', pkTest)

    return render(request, 'editar_pregunta.html', { 'form': form })
    

def eliminar_pregunta(request, pkPregunta, pkTest):
    pregunta = get_object_or_404(Pregunta, pk=pkPregunta)
    pregunta.delete()
    messages.warning(request, 'La pregunta ha sido eliminada correctamente.')
    
    return redirect('ver_preguntas', pkTest)
