from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Olá {} de {} anos</h1>'.format(nome, idade))
def soma(request, vri, vrf):
    vr = vri+vrf
    return HttpResponse('A soma de {} e {} é: {}'.format(vri, vrf, vr))
def multi(request, vri, vrf):
    vr = vri*vrf
    return HttpResponse('A multiplicação de {} e {} é: {}'.format(vri, vrf, vr))
def divi(request, vri, vrf):
    vr = vri/vrf
    return HttpResponse('A soma de {} e {} é: {}'.format(vri, vrf, vr))
def subt(request, vri, vrf):
    vr = vri-vrf
    return HttpResponse('A soma de {} e {} é: {}'.format(vri, vrf, vr))