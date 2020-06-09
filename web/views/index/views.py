from django.shortcuts import render


index_path = 'index/'


def index(request):
    return render(request, f'{index_path}index.html')
