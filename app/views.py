from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def pt(request):
    return HttpResponse('SANTOSH SIR')
def st(request):
    return HttpResponse('GREESHMA MAM')

def dt(request):
    return HttpResponse('HARSHAD SIR')