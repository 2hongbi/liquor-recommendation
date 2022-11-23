from django.shortcuts import render


def index(request):
    return render(request, 'beer/index.html')


def ver1(request):
    return render(request, 'beer/ver1.html')


def ver2(request):
    return render(request, 'beer/ver2.html')